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
from openapi_client.models.inline_response20019 import InlineResponse20019  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20019(unittest.TestCase):
    """InlineResponse20019 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20019
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20019.InlineResponse20019()  # noqa: E501
        if include_optional :
            return InlineResponse20019(
                id = 56, 
                files = -2147483648, 
                blank = -2147483648, 
                comment = -2147483648, 
                code = -2147483648, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                language = 56, 
                product = 56, 
                user = 56, 
                prefetch = openapi_client.models.inline_response_200_18_prefetch.inline_response_200_18_prefetch(
                    language = {
                        'key' : openapi_client.models.language_type.LanguageType(
                            id = 56, 
                            language = '0', 
                            color = '0', )
                        }, 
                    product = {
                        'key' : openapi_client.models.product.Product(
                            id = 56, 
                            findings_count = 56, 
                            findings_list = [
                                56
                                ], 
                            tags = [
                                '0'
                                ], 
                            product_meta = [
                                openapi_client.models.product_meta.ProductMeta(
                                    name = '0', 
                                    value = '0', )
                                ], 
                            name = '0', 
                            description = '0', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            prod_numeric_grade = -2147483648, 
                            business_criticality = 'very high', 
                            platform = 'web service', 
                            lifecycle = 'construction', 
                            origin = 'third party library', 
                            user_records = 0, 
                            revenue = '0', 
                            external_audience = True, 
                            internet_accessible = True, 
                            enable_simple_risk_acceptance = True, 
                            enable_full_risk_acceptance = True, 
                            product_manager = 56, 
                            technical_contact = 56, 
                            team_manager = 56, 
                            prod_type = 56, 
                            members = [
                                56
                                ], 
                            authorization_groups = [
                                56
                                ], 
                            regulations = [
                                56
                                ], )
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
            return InlineResponse20019(
                language = 56,
                product = 56,
        )

    def testInlineResponse20019(self):
        """Test InlineResponse20019"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
