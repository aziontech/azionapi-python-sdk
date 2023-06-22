import typing_extensions

from edgefirewall.paths import PathValues
from edgefirewall.apis.paths.edge_firewall import EdgeFirewall
from edgefirewall.apis.paths.edge_firewall_uuid import EdgeFirewallUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EDGE_FIREWALL: EdgeFirewall,
        PathValues.EDGE_FIREWALL_UUID: EdgeFirewallUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EDGE_FIREWALL: EdgeFirewall,
        PathValues.EDGE_FIREWALL_UUID: EdgeFirewallUuid,
    }
)
