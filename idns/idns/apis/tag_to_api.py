import typing_extensions

from idns.apis.tags import TagValues
from idns.apis.tags.zones_api import ZonesApi
from idns.apis.tags.records_api import RecordsApi
from idns.apis.tags.dnssec_api import DNSSECApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ZONES: ZonesApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.DNSSEC: DNSSECApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ZONES: ZonesApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.DNSSEC: DNSSECApi,
    }
)
