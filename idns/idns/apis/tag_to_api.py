import typing_extensions

from idns.apis.tags import TagValues
from idns.apis.tags.dnssec_api import DNSSECApi
from idns.apis.tags.records_api import RecordsApi
from idns.apis.tags.zones_api import ZonesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DNSSEC: DNSSECApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ZONES: ZonesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DNSSEC: DNSSECApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ZONES: ZonesApi,
    }
)
