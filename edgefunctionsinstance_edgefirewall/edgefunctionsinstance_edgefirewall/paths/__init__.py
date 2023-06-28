# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgefunctionsinstance_edgefirewall.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES = "/edge_firewall/:edge_firewall_id:/functions_instances"
    EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES_UUID = "/edge_firewall/:edge_firewall_id:/functions_instances/{uuid}"