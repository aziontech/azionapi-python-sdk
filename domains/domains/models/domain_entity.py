# coding: utf-8

"""
    Domain API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from domains.models.domain_data_digital_certificate_id import DomainDataDigitalCertificateId
from typing import Optional, Set
from typing_extensions import Self

class DomainEntity(BaseModel):
    """
    DomainEntity
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = None
    cnames: Optional[List[StrictStr]] = None
    cname_access_only: Optional[StrictBool] = None
    is_active: Optional[StrictBool] = None
    edge_application_id: Optional[Annotated[int, Field(le=-8446744073709551616, strict=True, ge=1)]] = None
    digital_certificate_id: Optional[DomainDataDigitalCertificateId] = None
    environment: Optional[StrictStr] = None
    is_mtls_enabled: Optional[StrictBool] = None
    mtls_trusted_ca_certificate_id: Optional[StrictInt] = None
    edge_firewall_id: Optional[StrictInt] = None
    mtls_verification: Optional[StrictStr] = None
    crl_list: Optional[List[StrictInt]] = None
    id: Optional[StrictInt] = None
    domain_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "cnames", "cname_access_only", "is_active", "edge_application_id", "digital_certificate_id", "environment", "is_mtls_enabled", "mtls_trusted_ca_certificate_id", "edge_firewall_id", "mtls_verification", "crl_list", "id", "domain_name"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9$%^&*()-+=\[\]{};:?><,|\/]+", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9$%^&*()-+=\[\]{};:?><,|\/]+/")
        return value

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['production', 'preview']):
            raise ValueError("must be one of enum values ('production', 'preview')")
        return value

    @field_validator('mtls_verification')
    def mtls_verification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enforce', 'permissive']):
            raise ValueError("must be one of enum values ('enforce', 'permissive')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DomainEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of digital_certificate_id
        if self.digital_certificate_id:
            _dict['digital_certificate_id'] = self.digital_certificate_id.to_dict()
        # set to None if mtls_trusted_ca_certificate_id (nullable) is None
        # and model_fields_set contains the field
        if self.mtls_trusted_ca_certificate_id is None and "mtls_trusted_ca_certificate_id" in self.model_fields_set:
            _dict['mtls_trusted_ca_certificate_id'] = None

        # set to None if edge_firewall_id (nullable) is None
        # and model_fields_set contains the field
        if self.edge_firewall_id is None and "edge_firewall_id" in self.model_fields_set:
            _dict['edge_firewall_id'] = None

        # set to None if crl_list (nullable) is None
        # and model_fields_set contains the field
        if self.crl_list is None and "crl_list" in self.model_fields_set:
            _dict['crl_list'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "cnames": obj.get("cnames"),
            "cname_access_only": obj.get("cname_access_only"),
            "is_active": obj.get("is_active"),
            "edge_application_id": obj.get("edge_application_id"),
            "digital_certificate_id": DomainDataDigitalCertificateId.from_dict(obj["digital_certificate_id"]) if obj.get("digital_certificate_id") is not None else None,
            "environment": obj.get("environment"),
            "is_mtls_enabled": obj.get("is_mtls_enabled"),
            "mtls_trusted_ca_certificate_id": obj.get("mtls_trusted_ca_certificate_id"),
            "edge_firewall_id": obj.get("edge_firewall_id"),
            "mtls_verification": obj.get("mtls_verification"),
            "crl_list": obj.get("crl_list"),
            "id": obj.get("id"),
            "domain_name": obj.get("domain_name")
        })
        return _obj


