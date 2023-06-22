# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgefirewall.paths.edge_firewall import Api

from edgefirewall.paths import PathValues

path = PathValues.EDGE_FIREWALL