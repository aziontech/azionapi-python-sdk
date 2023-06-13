# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from variables.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_SCHEMA = "/api/schema"
    API_VARIABLES = "/api/variables"
    API_VARIABLES_UUID = "/api/variables/{uuid}"
