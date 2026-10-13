"""Test harness for the generated Azion Python SDK packages.

The Vitest suite runs this script with the interpreter of a virtualenv that
has the package requirements installed. It never modifies generated code.

Usage:
  probe.py inspect <package_dir>
      Import the package, build Configuration and ApiClient, instantiate every
      generated API class and print them with their public methods as JSON.

  probe.py call <package_dir> <host> <api_key> <module> <class> <method> <kwargs_json>
      Call one generated API method against <host> and print the
      deserialized response as JSON.
"""
import datetime
import decimal
import importlib
import inspect
import json
import os
import pkgutil
import sys


def load(package_dir):
    package_dir = os.path.abspath(package_dir)
    name = os.path.basename(package_dir)
    sys.path.insert(0, package_dir)
    return name, importlib.import_module(name)


def api_modules(name, pkg):
    """Yield the generated API modules: `<pkg>.api.*` for the pydantic
    generators, otherwise `<pkg>.apis.tags.*` (python generator, tag APIs).
    Some pydantic packages still carry an `apis/` tree left over from an
    older generator run; it is not part of their public surface."""
    base = os.path.dirname(pkg.__file__)
    sub = "api" if os.path.isdir(os.path.join(base, "api")) else os.path.join("apis", "tags")
    dotted = sub.replace(os.sep, ".")
    for info in pkgutil.iter_modules([os.path.join(base, sub)]):
        yield importlib.import_module(f"{name}.{dotted}.{info.name}")


def client(pkg, host, api_key=None):
    configuration = pkg.Configuration(host=host)
    if api_key is not None:
        configuration.api_key["tokenAuth"] = api_key
        configuration.api_key_prefix["tokenAuth"] = "Token"
    return pkg.ApiClient(configuration)


def plain(value):
    """Convert SDK response objects into JSON-serializable data."""
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return plain(value.to_dict())
    if hasattr(value, "is_none_oapg") and value.is_none_oapg():
        return None
    if hasattr(value, "is_true_oapg") and value.is_true_oapg():
        return True
    if hasattr(value, "is_false_oapg") and value.is_false_oapg():
        return False
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if isinstance(value, decimal.Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def inspect_package(package_dir):
    name, pkg = load(package_dir)
    apis = {}
    with client(pkg, "http://127.0.0.1:9") as api_client:
        for module in api_modules(name, pkg):
            for cls_name, cls in inspect.getmembers(module, inspect.isclass):
                if cls.__module__ != module.__name__ or not cls_name.endswith("Api"):
                    continue
                instance = cls(api_client)
                methods = sorted(
                    m for m, _ in inspect.getmembers(instance, inspect.ismethod)
                    if not m.startswith("_")
                )
                apis[cls_name] = methods
    return {"package": name, "version": getattr(pkg, "__version__", None), "apis": apis}


def call(package_dir, host, api_key, module_name, cls_name, method, kwargs_json):
    name, pkg = load(package_dir)
    module = importlib.import_module(f"{name}.{module_name}")
    kwargs = json.loads(kwargs_json)
    with client(pkg, host, api_key) as api_client:
        api = getattr(module, cls_name)(api_client)
        response = getattr(api, method)(**kwargs)
    # The python (oapg) generator wraps the payload in ApiResponse.body.
    body = response.body if hasattr(response, "body") and hasattr(response, "response") else response
    return {"type": type(body).__name__, "data": plain(body)}


def main(argv):
    if len(argv) >= 2 and argv[0] == "inspect":
        result = inspect_package(argv[1])
    elif len(argv) == 8 and argv[0] == "call":
        result = call(*argv[1:])
    else:
        print(__doc__, file=sys.stderr)
        return 2
    json.dump(result, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
