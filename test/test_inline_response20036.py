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
from openapi_client.models.inline_response20036 import InlineResponse20036  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20036(unittest.TestCase):
    """InlineResponse20036 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20036
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20036.InlineResponse20036()  # noqa: E501
        if include_optional :
            return InlineResponse20036(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.product_type.ProductType(
                        id = 56, 
                        name = '0', 
                        description = '0', 
                        critical_product = True, 
                        key_product = True, 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        members = [
                            56
                            ], 
                        authorization_groups = [
                            56
                            ], )
                    ], 
                prefetch = openapi_client.models.inline_response_200_36_prefetch.inline_response_200_36_prefetch(
                    authorization_groups = {
                        'key' : openapi_client.models.dojo_group.DojoGroup(
                            id = 56, 
                            name = '0', 
                            description = '0', 
                            users = [
                                56
                                ], )
                        }, 
                    members = {
                        'key' : openapi_client.models.user_stub.UserStub(
                            id = 56, 
                            username = 'a', 
                            first_name = '0', 
                            last_name = '0', )
                        }, )
            )
        else :
            return InlineResponse20036(
                count = 56,
                results = [
                    openapi_client.models.product_type.ProductType(
                        id = 56, 
                        name = '0', 
                        description = '0', 
                        critical_product = True, 
                        key_product = True, 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        members = [
                            56
                            ], 
                        authorization_groups = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse20036(self):
        """Test InlineResponse20036"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()