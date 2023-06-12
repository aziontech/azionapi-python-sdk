from domains.paths.domains_id.get import ApiForget
from domains.paths.domains_id.put import ApiForput
from domains.paths.domains_id.delete import ApiFordelete
from domains.paths.domains_id.patch import ApiForpatch


class DomainsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
