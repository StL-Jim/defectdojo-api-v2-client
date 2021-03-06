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
from openapi_client.api.sonarqube_issues_api import SonarqubeIssuesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSonarqubeIssuesApi(unittest.TestCase):
    """SonarqubeIssuesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.sonarqube_issues_api.SonarqubeIssuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sonarqube_issues_create(self):
        """Test case for sonarqube_issues_create

        """
        pass

    def test_sonarqube_issues_delete(self):
        """Test case for sonarqube_issues_delete

        """
        pass

    def test_sonarqube_issues_list(self):
        """Test case for sonarqube_issues_list

        """
        pass

    def test_sonarqube_issues_partial_update(self):
        """Test case for sonarqube_issues_partial_update

        """
        pass

    def test_sonarqube_issues_read(self):
        """Test case for sonarqube_issues_read

        """
        pass

    def test_sonarqube_issues_update(self):
        """Test case for sonarqube_issues_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
