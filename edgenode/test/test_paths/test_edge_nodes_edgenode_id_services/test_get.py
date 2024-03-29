# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edgenode
from edgenode.paths.edge_nodes_edgenode_id_services import get  # noqa: E501
from edgenode import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeNodesEdgenodeIdServices(ApiTestMixin, unittest.TestCase):
    """
    EdgeNodesEdgenodeIdServices unit test stubs
        Return edge-node Services association  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
