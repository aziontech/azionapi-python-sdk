# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from data_streaming.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DATA_STREAMING = "Data Streaming"
    DATA_STREAMING_DOMAIN = "Data Streaming Domain"
    DATA_STREAMING_TEMPLATES = "Data Streaming Templates"
