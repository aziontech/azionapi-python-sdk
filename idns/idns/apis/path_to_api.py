import typing_extensions

from idns.paths import PathValues
from idns.apis.paths.intelligent_dns import IntelligentDns
from idns.apis.paths.intelligent_dns_zone_id import IntelligentDnsZoneId
from idns.apis.paths.intelligent_dns_zone_id_records import IntelligentDnsZoneIdRecords
from idns.apis.paths.intelligent_dns_zone_id_records_record_id import IntelligentDnsZoneIdRecordsRecordId
from idns.apis.paths.intelligent_dns_zone_id_dnssec import IntelligentDnsZoneIdDnssec

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.INTELLIGENT_DNS: IntelligentDns,
        PathValues.INTELLIGENT_DNS_ZONE_ID: IntelligentDnsZoneId,
        PathValues.INTELLIGENT_DNS_ZONE_ID_RECORDS: IntelligentDnsZoneIdRecords,
        PathValues.INTELLIGENT_DNS_ZONE_ID_RECORDS_RECORD_ID: IntelligentDnsZoneIdRecordsRecordId,
        PathValues.INTELLIGENT_DNS_ZONE_ID_DNSSEC: IntelligentDnsZoneIdDnssec,
    }
)

path_to_api = PathToApi(
    {
        PathValues.INTELLIGENT_DNS: IntelligentDns,
        PathValues.INTELLIGENT_DNS_ZONE_ID: IntelligentDnsZoneId,
        PathValues.INTELLIGENT_DNS_ZONE_ID_RECORDS: IntelligentDnsZoneIdRecords,
        PathValues.INTELLIGENT_DNS_ZONE_ID_RECORDS_RECORD_ID: IntelligentDnsZoneIdRecordsRecordId,
        PathValues.INTELLIGENT_DNS_ZONE_ID_DNSSEC: IntelligentDnsZoneIdDnssec,
    }
)
