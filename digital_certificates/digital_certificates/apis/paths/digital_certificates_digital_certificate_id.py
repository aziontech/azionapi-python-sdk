from digital_certificates.paths.digital_certificates_digital_certificate_id.get import ApiForget
from digital_certificates.paths.digital_certificates_digital_certificate_id.put import ApiForput
from digital_certificates.paths.digital_certificates_digital_certificate_id.delete import ApiFordelete
from digital_certificates.paths.digital_certificates_digital_certificate_id.patch import ApiForpatch


class DigitalCertificatesDigitalCertificateId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
