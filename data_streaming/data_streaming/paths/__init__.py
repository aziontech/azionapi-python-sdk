# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from data_streaming.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DATA_STREAMING_STREAMINGS = "/data_streaming/streamings"
    DATA_STREAMING_DOMAINS = "/data_streaming/domains"
    DATA_STREAMING_STREAMINGS_DATA_STREAMING_ID = "/data_streaming/streamings/{data_streaming_id}"
    DATA_STREAMING_TEMPLATES = "/data_streaming/templates"
    DATA_STREAMING_TEMPLATES_TEMPLATE_ID = "/data_streaming/templates/{template_id}"
