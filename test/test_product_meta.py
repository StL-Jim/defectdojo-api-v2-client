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
from openapi_client.models.product_meta import ProductMeta  # noqa: E501
from openapi_client.rest import ApiException

class TestProductMeta(unittest.TestCase):
    """ProductMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.product_meta.ProductMeta()  # noqa: E501
        if include_optional :
            return ProductMeta(
                name = '0', 
                value = '0'
            )
        else :
            return ProductMeta(
                name = '0',
                value = '0',
        )

    def testProductMeta(self):
        """Test ProductMeta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
