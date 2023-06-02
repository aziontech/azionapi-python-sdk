from idns.paths.intelligent_dns_zone_id.get import ApiForget
from idns.paths.intelligent_dns_zone_id.put import ApiForput
from idns.paths.intelligent_dns_zone_id.delete import ApiFordelete


class IntelligentDnsZoneId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
