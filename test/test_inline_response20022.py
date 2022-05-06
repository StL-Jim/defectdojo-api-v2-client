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
from openapi_client.models.inline_response20022 import InlineResponse20022  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20022(unittest.TestCase):
    """InlineResponse20022 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20022
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20022.InlineResponse20022()  # noqa: E501
        if include_optional :
            return InlineResponse20022(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.network_locations.NetworkLocations(
                        id = 56, 
                        location = '0', )
                    ]
            )
        else :
            return InlineResponse20022(
                count = 56,
                results = [
                    openapi_client.models.network_locations.NetworkLocations(
                        id = 56, 
                        location = '0', )
                    ],
        )

    def testInlineResponse20022(self):
        """Test InlineResponse20022"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
