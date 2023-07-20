# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from digital_certificates.paths.digital_certificates_csr import Api

from digital_certificates.paths import PathValues

path = PathValues.DIGITAL_CERTIFICATES_CSR