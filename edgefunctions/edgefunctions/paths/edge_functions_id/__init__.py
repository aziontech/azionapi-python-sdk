# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgefunctions.paths.edge_functions_id import Api

from edgefunctions.paths import PathValues

path = PathValues.EDGE_FUNCTIONS_ID