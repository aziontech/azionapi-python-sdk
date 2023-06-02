# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from realtimepurge.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from realtimepurge.model.purge_cache_key_request import PurgeCacheKeyRequest
from realtimepurge.model.purge_url_request import PurgeUrlRequest
from realtimepurge.model.purge_wildcard_request import PurgeWildcardRequest
