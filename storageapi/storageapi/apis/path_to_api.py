import typing_extensions

from storageapi.paths import PathValues
from storageapi.apis.paths.storage_version_id import StorageVersionId
from storageapi.apis.paths.storage_version_id_delete import StorageVersionIdDelete

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.STORAGE_VERSION_ID: StorageVersionId,
        PathValues.STORAGE_VERSION_ID_DELETE: StorageVersionIdDelete,
    }
)

path_to_api = PathToApi(
    {
        PathValues.STORAGE_VERSION_ID: StorageVersionId,
        PathValues.STORAGE_VERSION_ID_DELETE: StorageVersionIdDelete,
    }
)
