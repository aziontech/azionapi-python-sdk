# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from services.paths.edge_services import Api

from services.paths import PathValues

path = PathValues.EDGE_SERVICES