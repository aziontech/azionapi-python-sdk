import typing_extensions

from domains.paths import PathValues
from domains.apis.paths.domains import Domains
from domains.apis.paths.domains_id import DomainsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_ID: DomainsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_ID: DomainsId,
    }
)
