# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from edgeapplications.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from edgeapplications.model.application_cache_create_request import ApplicationCacheCreateRequest
from edgeapplications.model.application_cache_create_response import ApplicationCacheCreateResponse
from edgeapplications.model.application_cache_create_results import ApplicationCacheCreateResults
from edgeapplications.model.application_cache_get_one_response import ApplicationCacheGetOneResponse
from edgeapplications.model.application_cache_get_response import ApplicationCacheGetResponse
from edgeapplications.model.application_cache_patch_request import ApplicationCachePatchRequest
from edgeapplications.model.application_cache_patch_response import ApplicationCachePatchResponse
from edgeapplications.model.application_cache_put_request import ApplicationCachePutRequest
from edgeapplications.model.application_cache_put_response import ApplicationCachePutResponse
from edgeapplications.model.application_cache_response_details import ApplicationCacheResponseDetails
from edgeapplications.model.application_cache_results import ApplicationCacheResults
from edgeapplications.model.application_create_instance_request import ApplicationCreateInstanceRequest
from edgeapplications.model.application_instance_results import ApplicationInstanceResults
from edgeapplications.model.application_instances_get_one_response import ApplicationInstancesGetOneResponse
from edgeapplications.model.application_instances_get_response import ApplicationInstancesGetResponse
from edgeapplications.model.application_instances_results import ApplicationInstancesResults
from edgeapplications.model.application_links import ApplicationLinks
from edgeapplications.model.application_origins import ApplicationOrigins
from edgeapplications.model.application_put_instance_request import ApplicationPutInstanceRequest
from edgeapplications.model.application_put_request import ApplicationPutRequest
from edgeapplications.model.application_put_result import ApplicationPutResult
from edgeapplications.model.application_results import ApplicationResults
from edgeapplications.model.application_results_create import ApplicationResultsCreate
from edgeapplications.model.application_update_instance_request import ApplicationUpdateInstanceRequest
from edgeapplications.model.application_update_request import ApplicationUpdateRequest
from edgeapplications.model.application_update_response import ApplicationUpdateResponse
from edgeapplications.model.application_update_results import ApplicationUpdateResults
from edgeapplications.model.applications_results import ApplicationsResults
from edgeapplications.model.create_application_request import CreateApplicationRequest
from edgeapplications.model.create_application_result import CreateApplicationResult
from edgeapplications.model.create_device_groups_request import CreateDeviceGroupsRequest
from edgeapplications.model.create_origins_request import CreateOriginsRequest
from edgeapplications.model.create_origins_request_addresses import CreateOriginsRequestAddresses
from edgeapplications.model.create_rules_engine_request import CreateRulesEngineRequest
from edgeapplications.model.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.model.device_groups_response import DeviceGroupsResponse
from edgeapplications.model.device_groups_response_links import DeviceGroupsResponseLinks
from edgeapplications.model.device_groups_result_response import DeviceGroupsResultResponse
from edgeapplications.model.get_application_response import GetApplicationResponse
from edgeapplications.model.origins_id_response import OriginsIdResponse
from edgeapplications.model.origins_response import OriginsResponse
from edgeapplications.model.origins_response_links import OriginsResponseLinks
from edgeapplications.model.origins_result_response import OriginsResultResponse
from edgeapplications.model.origins_result_response_addresses import OriginsResultResponseAddresses
from edgeapplications.model.patch_device_groups_request import PatchDeviceGroupsRequest
from edgeapplications.model.patch_origins_request import PatchOriginsRequest
from edgeapplications.model.patch_rules_engine_request import PatchRulesEngineRequest
from edgeapplications.model.rules_engine_behavior import RulesEngineBehavior
from edgeapplications.model.rules_engine_criteria import RulesEngineCriteria
from edgeapplications.model.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.model.rules_engine_response import RulesEngineResponse
from edgeapplications.model.rules_engine_result_response import RulesEngineResultResponse
from edgeapplications.model.rules_engine_result_response_behaviors import RulesEngineResultResponseBehaviors
from edgeapplications.model.update_device_groups_request import UpdateDeviceGroupsRequest
from edgeapplications.model.update_origins_request import UpdateOriginsRequest
from edgeapplications.model.update_rules_engine_request import UpdateRulesEngineRequest
