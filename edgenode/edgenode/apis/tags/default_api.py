# coding: utf-8

"""
    Edge Node API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from edgenode.paths.edge_nodes_authorize.patch import AuthorizeEdgeNode
from edgenode.paths.edge_nodes_edgenode_id_services.post import CreateEdgeNodeSvcs
from edgenode.paths.edge_nodes_edgenode_id.delete import DelEdgeNode
from edgenode.paths.edge_nodes_edgenode_id_services_bind_id.delete import DelEdgeNodeSvc
from edgenode.paths.edge_nodes_edgenode_id.get import GetEdgeNode
from edgenode.paths.edge_nodes_groups.get import GetEdgeNodeGroups
from edgenode.paths.edge_nodes_edgenode_id_services_bind_id.get import GetEdgeNodeSvcDetail
from edgenode.paths.edge_nodes_edgenode_id_services.get import GetEdgeNodeSvcs
from edgenode.paths.edge_nodes.get import GetEdgeNodes
from edgenode.paths.edge_nodes_edgenode_id.patch import UpdateEdgeNode
from edgenode.paths.edge_nodes_edgenode_id_services_bind_id.patch import UpdateEdgeNodeSvcDetail


class DefaultApi(
    AuthorizeEdgeNode,
    CreateEdgeNodeSvcs,
    DelEdgeNode,
    DelEdgeNodeSvc,
    GetEdgeNode,
    GetEdgeNodeGroups,
    GetEdgeNodeSvcDetail,
    GetEdgeNodeSvcs,
    GetEdgeNodes,
    UpdateEdgeNode,
    UpdateEdgeNodeSvcDetail,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
