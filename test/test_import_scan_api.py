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
from openapi_client.api.import_scan_api import ImportScanApi  # noqa: E501
from openapi_client.rest import ApiException


class TestImportScanApi(unittest.TestCase):
    """ImportScanApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.import_scan_api.ImportScanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_scan_create(self):
        """Test case for import_scan_create

        Imports a scan report into an engagement or product.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()