# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from idns.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    INTELLIGENT_DNS = "/intelligent_dns"
    INTELLIGENT_DNS_ZONE_ID = "/intelligent_dns/{zone_id}"
    INTELLIGENT_DNS_ZONE_ID_RECORDS = "/intelligent_dns/{zone_id}/records"
    INTELLIGENT_DNS_ZONE_ID_RECORDS_RECORD_ID = "/intelligent_dns/{zone_id}/records/{record_id}"
    INTELLIGENT_DNS_ZONE_ID_DNSSEC = "/intelligent_dns/{zone_id}/dnssec"
