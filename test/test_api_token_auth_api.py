# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.api_token_auth_api import ApiTokenAuthApi  # noqa: E501
from openapi_client.rest import ApiException


class TestApiTokenAuthApi(unittest.TestCase):
    """ApiTokenAuthApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.api_token_auth_api.ApiTokenAuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_token_auth_create(self):
        """Test case for api_token_auth_create

        """
        pass


if __name__ == '__main__':
    unittest.main()