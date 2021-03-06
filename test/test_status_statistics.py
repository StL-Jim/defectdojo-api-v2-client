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
from openapi_client.models.status_statistics import StatusStatistics  # noqa: E501
from openapi_client.rest import ApiException

class TestStatusStatistics(unittest.TestCase):
    """StatusStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatusStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.status_statistics.StatusStatistics()  # noqa: E501
        if include_optional :
            return StatusStatistics(
                active = 56, 
                verified = 56, 
                duplicate = 56, 
                false_p = 56, 
                out_of_scope = 56, 
                is_mitigated = 56, 
                risk_accepted = 56, 
                total = 56
            )
        else :
            return StatusStatistics(
                active = 56,
                verified = 56,
                duplicate = 56,
                false_p = 56,
                out_of_scope = 56,
                is_mitigated = 56,
                risk_accepted = 56,
                total = 56,
        )

    def testStatusStatistics(self):
        """Test StatusStatistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
