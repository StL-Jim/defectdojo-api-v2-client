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
from openapi_client.models.tool_product_settings import ToolProductSettings  # noqa: E501
from openapi_client.rest import ApiException

class TestToolProductSettings(unittest.TestCase):
    """ToolProductSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ToolProductSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.tool_product_settings.ToolProductSettings()  # noqa: E501
        if include_optional :
            return ToolProductSettings(
                id = 56, 
                setting_url = '0', 
                name = '0', 
                description = '0', 
                url = '0', 
                tool_project_id = '0', 
                product = 56, 
                tool_configuration = 56, 
                notes = [
                    56
                    ]
            )
        else :
            return ToolProductSettings(
                setting_url = '0',
                name = '0',
                tool_configuration = 56,
        )

    def testToolProductSettings(self):
        """Test ToolProductSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
