# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from waf.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    WAF_WAF_ID_DOMAINS = "/waf/{wafId}/domains"
    WAF_WAF_ID_WAF_EVENTS = "/waf/{wafId}/waf_events"
