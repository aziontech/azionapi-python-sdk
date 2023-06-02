# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgeapplications.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EDGE_APPLICATIONS__CACHE_SETTINGS = "Edge Applications &gt; Cache Settings"
    EDGE_APPLICATIONS__DEVICE_GROUPS = "Edge Applications &gt; Device Groups"
    EDGE_APPLICATIONS__EDGE_FUNCTIONS_INSTANCES = "Edge Applications &gt; Edge Functions Instances"
    EDGE_APPLICATIONS__MAIN_SETTINGS = "Edge Applications &gt; Main Settings"
    EDGE_APPLICATIONS__ORIGINS = "Edge Applications &gt; Origins"
    EDGE_APPLICATIONS__RULES_ENGINE = "Edge Applications &gt; Rules Engine"
