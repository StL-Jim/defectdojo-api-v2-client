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
from openapi_client.models.finding_engagement import FindingEngagement  # noqa: E501
from openapi_client.rest import ApiException

class TestFindingEngagement(unittest.TestCase):
    """FindingEngagement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindingEngagement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.finding_engagement.FindingEngagement()  # noqa: E501
        if include_optional :
            return FindingEngagement(
                id = 56, 
                name = '0', 
                product = openapi_client.models.finding_product.FindingProduct(
                    id = 56, 
                    name = '0', 
                    prod_type = openapi_client.models.finding_prod_type.FindingProdType(
                        id = 56, 
                        name = '0', ), ), 
                branch_tag = '0', 
                build_id = '0', 
                commit_hash = '0', 
                version = '0'
            )
        else :
            return FindingEngagement(
        )

    def testFindingEngagement(self):
        """Test FindingEngagement"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()