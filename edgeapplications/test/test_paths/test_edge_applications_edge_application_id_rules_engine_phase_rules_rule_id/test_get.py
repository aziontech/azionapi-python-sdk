# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edgeapplications
from edgeapplications.paths.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id import get  # noqa: E501
from edgeapplications import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeApplicationsEdgeApplicationIdRulesEnginePhaseRulesRuleId(ApiTestMixin, unittest.TestCase):
    """
    EdgeApplicationsEdgeApplicationIdRulesEnginePhaseRulesRuleId unit test stubs
        /edge_applications/{edge_application_id}/rules_engine/{phase}/rules  # noqa: E501
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
