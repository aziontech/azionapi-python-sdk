# coding: utf-8

# flake8: noqa

"""
    Edge Application API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from edgeapplications.api.edge_applications_cache_settings_api import EdgeApplicationsCacheSettingsApi
from edgeapplications.api.edge_applications_device_groups_api import EdgeApplicationsDeviceGroupsApi
from edgeapplications.api.edge_applications_edge_functions_instances_api import EdgeApplicationsEdgeFunctionsInstancesApi
from edgeapplications.api.edge_applications_main_settings_api import EdgeApplicationsMainSettingsApi
from edgeapplications.api.edge_applications_origins_api import EdgeApplicationsOriginsApi
from edgeapplications.api.edge_applications_rules_engine_api import EdgeApplicationsRulesEngineApi

# import ApiClient
from edgeapplications.api_response import ApiResponse
from edgeapplications.api_client import ApiClient
from edgeapplications.configuration import Configuration
from edgeapplications.exceptions import OpenApiException
from edgeapplications.exceptions import ApiTypeError
from edgeapplications.exceptions import ApiValueError
from edgeapplications.exceptions import ApiKeyError
from edgeapplications.exceptions import ApiAttributeError
from edgeapplications.exceptions import ApiException

# import models into sdk package
from edgeapplications.models.application_cache_create_request import ApplicationCacheCreateRequest
from edgeapplications.models.application_cache_create_response import ApplicationCacheCreateResponse
from edgeapplications.models.application_cache_create_results import ApplicationCacheCreateResults
from edgeapplications.models.application_cache_get_one_response import ApplicationCacheGetOneResponse
from edgeapplications.models.application_cache_get_response import ApplicationCacheGetResponse
from edgeapplications.models.application_cache_patch_request import ApplicationCachePatchRequest
from edgeapplications.models.application_cache_patch_response import ApplicationCachePatchResponse
from edgeapplications.models.application_cache_put_request import ApplicationCachePutRequest
from edgeapplications.models.application_cache_put_response import ApplicationCachePutResponse
from edgeapplications.models.application_cache_response_details import ApplicationCacheResponseDetails
from edgeapplications.models.application_cache_results import ApplicationCacheResults
from edgeapplications.models.application_create_instance_request import ApplicationCreateInstanceRequest
from edgeapplications.models.application_create_instance_request_args import ApplicationCreateInstanceRequestArgs
from edgeapplications.models.application_instance_results import ApplicationInstanceResults
from edgeapplications.models.application_instances_get_one_response import ApplicationInstancesGetOneResponse
from edgeapplications.models.application_instances_get_response import ApplicationInstancesGetResponse
from edgeapplications.models.application_instances_results import ApplicationInstancesResults
from edgeapplications.models.application_links import ApplicationLinks
from edgeapplications.models.application_origins import ApplicationOrigins
from edgeapplications.models.application_put_instance_request import ApplicationPutInstanceRequest
from edgeapplications.models.application_put_request import ApplicationPutRequest
from edgeapplications.models.application_put_result import ApplicationPutResult
from edgeapplications.models.application_results import ApplicationResults
from edgeapplications.models.application_results_create import ApplicationResultsCreate
from edgeapplications.models.application_update_instance_request import ApplicationUpdateInstanceRequest
from edgeapplications.models.application_update_request import ApplicationUpdateRequest
from edgeapplications.models.application_update_response import ApplicationUpdateResponse
from edgeapplications.models.application_update_results import ApplicationUpdateResults
from edgeapplications.models.applications_results import ApplicationsResults
from edgeapplications.models.create_application_request import CreateApplicationRequest
from edgeapplications.models.create_application_result import CreateApplicationResult
from edgeapplications.models.create_device_groups_request import CreateDeviceGroupsRequest
from edgeapplications.models.create_origins_request import CreateOriginsRequest
from edgeapplications.models.create_origins_request_addresses import CreateOriginsRequestAddresses
from edgeapplications.models.create_rules_engine_request import CreateRulesEngineRequest
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.models.device_groups_response import DeviceGroupsResponse
from edgeapplications.models.device_groups_response_links import DeviceGroupsResponseLinks
from edgeapplications.models.device_groups_result_response import DeviceGroupsResultResponse
from edgeapplications.models.get_application_response import GetApplicationResponse
from edgeapplications.models.get_applications_response import GetApplicationsResponse
from edgeapplications.models.origins_id_response import OriginsIdResponse
from edgeapplications.models.origins_response import OriginsResponse
from edgeapplications.models.origins_response_links import OriginsResponseLinks
from edgeapplications.models.origins_result_response import OriginsResultResponse
from edgeapplications.models.origins_result_response_addresses import OriginsResultResponseAddresses
from edgeapplications.models.patch_device_groups_request import PatchDeviceGroupsRequest
from edgeapplications.models.patch_origins_request import PatchOriginsRequest
from edgeapplications.models.patch_rules_engine_request import PatchRulesEngineRequest
from edgeapplications.models.rules_engine_behavior_entry import RulesEngineBehaviorEntry
from edgeapplications.models.rules_engine_behavior_object import RulesEngineBehaviorObject
from edgeapplications.models.rules_engine_behavior_object_target import RulesEngineBehaviorObjectTarget
from edgeapplications.models.rules_engine_behavior_string import RulesEngineBehaviorString
from edgeapplications.models.rules_engine_criteria import RulesEngineCriteria
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.models.rules_engine_response import RulesEngineResponse
from edgeapplications.models.rules_engine_result_response import RulesEngineResultResponse
from edgeapplications.models.update_device_groups_request import UpdateDeviceGroupsRequest
from edgeapplications.models.update_origins_request import UpdateOriginsRequest
from edgeapplications.models.update_rules_engine_request import UpdateRulesEngineRequest
