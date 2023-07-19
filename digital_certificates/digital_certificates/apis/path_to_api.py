import typing_extensions

from digital_certificates.paths import PathValues
from digital_certificates.apis.paths.digital_certificates import DigitalCertificates
from digital_certificates.apis.paths.digital_certificates_digital_certificate_id import DigitalCertificatesDigitalCertificateId
from digital_certificates.apis.paths.digital_certificates_csr import DigitalCertificatesCsr

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DIGITAL_CERTIFICATES: DigitalCertificates,
        PathValues.DIGITAL_CERTIFICATES_DIGITAL_CERTIFICATE_ID: DigitalCertificatesDigitalCertificateId,
        PathValues.DIGITAL_CERTIFICATES_CSR: DigitalCertificatesCsr,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DIGITAL_CERTIFICATES: DigitalCertificates,
        PathValues.DIGITAL_CERTIFICATES_DIGITAL_CERTIFICATE_ID: DigitalCertificatesDigitalCertificateId,
        PathValues.DIGITAL_CERTIFICATES_CSR: DigitalCertificatesCsr,
    }
)
