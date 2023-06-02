# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from realtimepurge.paths.purge_wildcard import Api

from realtimepurge.paths import PathValues

path = PathValues.PURGE_WILDCARD