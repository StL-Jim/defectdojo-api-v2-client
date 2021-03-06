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
from openapi_client.models.inline_response2007 import InlineResponse2007  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2007(unittest.TestCase):
    """InlineResponse2007 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2007
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2007.InlineResponse2007()  # noqa: E501
        if include_optional :
            return InlineResponse2007(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.engagement_presets.EngagementPresets(
                        id = 56, 
                        title = '0', 
                        notes = '0', 
                        scope = '0', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product = 56, 
                        test_type = [
                            56
                            ], 
                        network_locations = [
                            56
                            ], )
                    ]
            )
        else :
            return InlineResponse2007(
                count = 56,
                results = [
                    openapi_client.models.engagement_presets.EngagementPresets(
                        id = 56, 
                        title = '0', 
                        notes = '0', 
                        scope = '0', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product = 56, 
                        test_type = [
                            56
                            ], 
                        network_locations = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse2007(self):
        """Test InlineResponse2007"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
