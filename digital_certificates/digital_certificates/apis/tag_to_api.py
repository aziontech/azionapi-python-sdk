import typing_extensions

from digital_certificates.apis.tags import TagValues
from digital_certificates.apis.tags.create_csr_api import CreateCSRApi
from digital_certificates.apis.tags.create_digital_certificate_api import CreateDigitalCertificateApi
from digital_certificates.apis.tags.delete_digital_certificate_api import DeleteDigitalCertificateApi
from digital_certificates.apis.tags.overwrite_digital_certificate_api import OverwriteDigitalCertificateApi
from digital_certificates.apis.tags.retrieve_digital_certificate_by_id_api import RetrieveDigitalCertificateByIDApi
from digital_certificates.apis.tags.retrieve_digital_certificate_list_api import RetrieveDigitalCertificateListApi
from digital_certificates.apis.tags.update_digital_certificate_api import UpdateDigitalCertificateApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CREATE_CSR: CreateCSRApi,
        TagValues.CREATE_DIGITAL_CERTIFICATE: CreateDigitalCertificateApi,
        TagValues.DELETE_DIGITAL_CERTIFICATE: DeleteDigitalCertificateApi,
        TagValues.OVERWRITE_DIGITAL_CERTIFICATE: OverwriteDigitalCertificateApi,
        TagValues.RETRIEVE_DIGITAL_CERTIFICATE_BY_ID: RetrieveDigitalCertificateByIDApi,
        TagValues.RETRIEVE_DIGITAL_CERTIFICATE_LIST: RetrieveDigitalCertificateListApi,
        TagValues.UPDATE_DIGITAL_CERTIFICATE: UpdateDigitalCertificateApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CREATE_CSR: CreateCSRApi,
        TagValues.CREATE_DIGITAL_CERTIFICATE: CreateDigitalCertificateApi,
        TagValues.DELETE_DIGITAL_CERTIFICATE: DeleteDigitalCertificateApi,
        TagValues.OVERWRITE_DIGITAL_CERTIFICATE: OverwriteDigitalCertificateApi,
        TagValues.RETRIEVE_DIGITAL_CERTIFICATE_BY_ID: RetrieveDigitalCertificateByIDApi,
        TagValues.RETRIEVE_DIGITAL_CERTIFICATE_LIST: RetrieveDigitalCertificateListApi,
        TagValues.UPDATE_DIGITAL_CERTIFICATE: UpdateDigitalCertificateApi,
    }
)
