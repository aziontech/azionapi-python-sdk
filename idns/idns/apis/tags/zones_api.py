# coding: utf-8

"""
    Intelligent DNS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from idns.paths.intelligent_dns_zone_id.delete import DeleteZone
from idns.paths.intelligent_dns_zone_id.get import GetZone
from idns.paths.intelligent_dns.get import GetZones
from idns.paths.intelligent_dns.post import PostZone
from idns.paths.intelligent_dns_zone_id.put import PutZone


class ZonesApi(
    DeleteZone,
    GetZone,
    GetZones,
    PostZone,
    PutZone,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
