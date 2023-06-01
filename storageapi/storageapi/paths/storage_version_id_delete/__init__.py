# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from storageapi.paths.storage_version_id_delete import Api

from storageapi.paths import PathValues

path = PathValues.STORAGE_VERSION_ID_DELETE