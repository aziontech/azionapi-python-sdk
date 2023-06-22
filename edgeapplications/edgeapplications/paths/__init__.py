# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgeapplications.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EDGE_APPLICATIONS = "/edge_applications"
    EDGE_APPLICATIONS_ID = "/edge_applications/{id}"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_CACHE_SETTINGS = "/edge_applications/{edge_application_id}/cache_settings"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_CACHE_SETTINGS_CACHE_SETTINGS_ID = "/edge_applications/{edge_application_id}/cache_settings/{cache_settings_id}"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_FUNCTIONS_INSTANCES = "/edge_applications/{edge_application_id}/functions_instances"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_FUNCTIONS_INSTANCES_FUNCTIONS_INSTANCES_ID = "/edge_applications/{edge_application_id}/functions_instances/{functions_instances_id}"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_ORIGINS = "/edge_applications/{edge_application_id}/origins"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_ORIGINS_ORIGIN_KEY = "/edge_applications/{edge_application_id}/origins/{origin_key}"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_RULES_ENGINE_PHASE_RULES = "/edge_applications/{edge_application_id}/rules_engine/{phase}/rules"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_RULES_ENGINE_PHASE_RULES_RULE_ID = "/edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id}"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_DEVICE_GROUPS = "/edge_applications/{edge_application_id}/device_groups"
    EDGE_APPLICATIONS_EDGE_APPLICATION_ID_DEVICE_GROUPS_DEVICE_GROUP_ID = "/edge_applications/{edge_application_id}/device_groups/{device_group_id}"
