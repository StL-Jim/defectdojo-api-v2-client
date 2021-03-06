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
from openapi_client.models.engagement_to_files import EngagementToFiles  # noqa: E501
from openapi_client.rest import ApiException

class TestEngagementToFiles(unittest.TestCase):
    """EngagementToFiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EngagementToFiles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.engagement_to_files.EngagementToFiles()  # noqa: E501
        if include_optional :
            return EngagementToFiles(
                engagement_id = 56, 
                files = [
                    openapi_client.models.file.File(
                        id = 56, 
                        file = '0', 
                        title = '0', )
                    ]
            )
        else :
            return EngagementToFiles(
                engagement_id = 56,
                files = [
                    openapi_client.models.file.File(
                        id = 56, 
                        file = '0', 
                        title = '0', )
                    ],
        )

    def testEngagementToFiles(self):
        """Test EngagementToFiles"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
