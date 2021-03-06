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
from openapi_client.models.inline_response20012 import InlineResponse20012  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20012(unittest.TestCase):
    """InlineResponse20012 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20012
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20012.InlineResponse20012()  # noqa: E501
        if include_optional :
            return InlineResponse20012(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.global_role.GlobalRole(
                        id = 56, 
                        user = 56, 
                        group = 56, 
                        role = 56, )
                    ], 
                prefetch = openapi_client.models.inline_response_200_1_prefetch.inline_response_200_1_prefetch(
                    group = {
                        'key' : openapi_client.models.dojo_group.DojoGroup(
                            id = 56, 
                            name = '0', 
                            description = '0', 
                            users = [
                                56
                                ], )
                        }, 
                    role = {
                        'key' : openapi_client.models.role.Role(
                            id = 56, 
                            name = '0', 
                            is_owner = True, )
                        }, 
                    user = {
                        'key' : openapi_client.models.user_stub.UserStub(
                            id = 56, 
                            username = 'a', 
                            first_name = '0', 
                            last_name = '0', )
                        }, )
            )
        else :
            return InlineResponse20012(
                count = 56,
                results = [
                    openapi_client.models.global_role.GlobalRole(
                        id = 56, 
                        user = 56, 
                        group = 56, 
                        role = 56, )
                    ],
        )

    def testInlineResponse20012(self):
        """Test InlineResponse20012"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
