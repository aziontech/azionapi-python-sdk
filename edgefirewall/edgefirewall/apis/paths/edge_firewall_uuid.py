from edgefirewall.paths.edge_firewall_uuid.get import ApiForget
from edgefirewall.paths.edge_firewall_uuid.put import ApiForput
from edgefirewall.paths.edge_firewall_uuid.delete import ApiFordelete
from edgefirewall.paths.edge_firewall_uuid.patch import ApiForpatch


class EdgeFirewallUuid(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
