import typing_extensions

from waf.paths import PathValues
from waf.apis.paths.waf_waf_id_domains import WafWafIdDomains
from waf.apis.paths.waf_waf_id_waf_events import WafWafIdWafEvents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.WAF_WAF_ID_DOMAINS: WafWafIdDomains,
        PathValues.WAF_WAF_ID_WAF_EVENTS: WafWafIdWafEvents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.WAF_WAF_ID_DOMAINS: WafWafIdDomains,
        PathValues.WAF_WAF_ID_WAF_EVENTS: WafWafIdWafEvents,
    }
)
