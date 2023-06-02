import typing_extensions

from edgeapplications.apis.tags import TagValues
from edgeapplications.apis.tags.edge_applications_cache_settings_api import EdgeApplicationsCacheSettingsApi
from edgeapplications.apis.tags.edge_applications_device_groups_api import EdgeApplicationsDeviceGroupsApi
from edgeapplications.apis.tags.edge_applications_edge_functions_instances_api import EdgeApplicationsEdgeFunctionsInstancesApi
from edgeapplications.apis.tags.edge_applications_main_settings_api import EdgeApplicationsMainSettingsApi
from edgeapplications.apis.tags.edge_applications_origins_api import EdgeApplicationsOriginsApi
from edgeapplications.apis.tags.edge_applications_rules_engine_api import EdgeApplicationsRulesEngineApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EDGE_APPLICATIONS__CACHE_SETTINGS: EdgeApplicationsCacheSettingsApi,
        TagValues.EDGE_APPLICATIONS__DEVICE_GROUPS: EdgeApplicationsDeviceGroupsApi,
        TagValues.EDGE_APPLICATIONS__EDGE_FUNCTIONS_INSTANCES: EdgeApplicationsEdgeFunctionsInstancesApi,
        TagValues.EDGE_APPLICATIONS__MAIN_SETTINGS: EdgeApplicationsMainSettingsApi,
        TagValues.EDGE_APPLICATIONS__ORIGINS: EdgeApplicationsOriginsApi,
        TagValues.EDGE_APPLICATIONS__RULES_ENGINE: EdgeApplicationsRulesEngineApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EDGE_APPLICATIONS__CACHE_SETTINGS: EdgeApplicationsCacheSettingsApi,
        TagValues.EDGE_APPLICATIONS__DEVICE_GROUPS: EdgeApplicationsDeviceGroupsApi,
        TagValues.EDGE_APPLICATIONS__EDGE_FUNCTIONS_INSTANCES: EdgeApplicationsEdgeFunctionsInstancesApi,
        TagValues.EDGE_APPLICATIONS__MAIN_SETTINGS: EdgeApplicationsMainSettingsApi,
        TagValues.EDGE_APPLICATIONS__ORIGINS: EdgeApplicationsOriginsApi,
        TagValues.EDGE_APPLICATIONS__RULES_ENGINE: EdgeApplicationsRulesEngineApi,
    }
)
