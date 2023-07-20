# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from digital_certificates.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DIGITAL_CERTIFICATES = "/digital_certificates"
    DIGITAL_CERTIFICATES_DIGITAL_CERTIFICATE_ID = "/digital_certificates/{digital_certificate_id}"
    DIGITAL_CERTIFICATES_CSR = "/digital_certificates/csr"
