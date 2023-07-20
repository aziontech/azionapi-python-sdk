# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from digital_certificates.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CREATE_CSR = "Create CSR"
    CREATE_DIGITAL_CERTIFICATE = "Create digital certificate"
    DELETE_DIGITAL_CERTIFICATE = "Delete digital certificate"
    OVERWRITE_DIGITAL_CERTIFICATE = "Overwrite digital certificate"
    RETRIEVE_DIGITAL_CERTIFICATE_BY_ID = "Retrieve digital certificate by ID"
    RETRIEVE_DIGITAL_CERTIFICATE_LIST = "Retrieve digital certificate list"
    UPDATE_DIGITAL_CERTIFICATE = "Update digital certificate"
