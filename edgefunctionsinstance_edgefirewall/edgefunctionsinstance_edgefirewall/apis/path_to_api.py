import typing_extensions

from edgefunctionsinstance_edgefirewall.paths import PathValues
from edgefunctionsinstance_edgefirewall.apis.paths.edge_firewall_edge_firewall_id_functions_instances import EdgeFirewallEdgeFirewallIdFunctionsInstances
from edgefunctionsinstance_edgefirewall.apis.paths.edge_firewall_edge_firewall_id_functions_instances_uuid import EdgeFirewallEdgeFirewallIdFunctionsInstancesUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES: EdgeFirewallEdgeFirewallIdFunctionsInstances,
        PathValues.EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES_UUID: EdgeFirewallEdgeFirewallIdFunctionsInstancesUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES: EdgeFirewallEdgeFirewallIdFunctionsInstances,
        PathValues.EDGE_FIREWALL_EDGE_FIREWALL_ID_FUNCTIONS_INSTANCES_UUID: EdgeFirewallEdgeFirewallIdFunctionsInstancesUuid,
    }
)
