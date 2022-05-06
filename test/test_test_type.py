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
from openapi_client.models.test_type import TestType  # noqa: E501
from openapi_client.rest import ApiException

class TestTestType(unittest.TestCase):
    """TestType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.test_type.TestType()  # noqa: E501
        if include_optional :
            return TestType(
                id = 56, 
                tags = [
                    '0'
                    ], 
                name = '0', 
                static_tool = True, 
                dynamic_tool = True, 
                active = True
            )
        else :
            return TestType(
                name = '0',
        )

    def testTestType(self):
        """Test TestType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
