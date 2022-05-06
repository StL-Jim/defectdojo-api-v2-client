# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.executive_summary import ExecutiveSummary  # noqa: E501
from openapi_client.rest import ApiException

class TestExecutiveSummary(unittest.TestCase):
    """ExecutiveSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExecutiveSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.executive_summary.ExecutiveSummary()  # noqa: E501
        if include_optional :
            return ExecutiveSummary(
                engagement_name = '0', 
                engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                test_type_name = '0', 
                test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                test_environment_name = '0', 
                test_strategy_ref = '0', 
                total_findings = 56
            )
        else :
            return ExecutiveSummary(
                engagement_name = '0',
                engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                test_type_name = '0',
                test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                test_environment_name = '0',
                test_strategy_ref = '0',
                total_findings = 56,
        )

    def testExecutiveSummary(self):
        """Test ExecutiveSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
