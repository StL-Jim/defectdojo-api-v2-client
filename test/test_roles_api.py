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
from openapi_client.api.roles_api import RolesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_roles_list(self):
        """Test case for roles_list

        """
        pass

    def test_roles_read(self):
        """Test case for roles_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
