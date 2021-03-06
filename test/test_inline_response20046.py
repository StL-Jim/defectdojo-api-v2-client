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
from openapi_client.models.inline_response20046 import InlineResponse20046  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20046(unittest.TestCase):
    """InlineResponse20046 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20046
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20046.InlineResponse20046()  # noqa: E501
        if include_optional :
            return InlineResponse20046(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.app_analysis.AppAnalysis(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        name = '0', 
                        confidence = -2147483648, 
                        version = '0', 
                        icon = '0', 
                        website = '0', 
                        website_found = '0', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product = 56, 
                        user = 56, )
                    ]
            )
        else :
            return InlineResponse20046(
                count = 56,
                results = [
                    openapi_client.models.app_analysis.AppAnalysis(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        name = '0', 
                        confidence = -2147483648, 
                        version = '0', 
                        icon = '0', 
                        website = '0', 
                        website_found = '0', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product = 56, 
                        user = 56, )
                    ],
        )

    def testInlineResponse20046(self):
        """Test InlineResponse20046"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
