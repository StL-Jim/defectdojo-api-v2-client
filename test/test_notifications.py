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
from openapi_client.models.notifications import Notifications  # noqa: E501
from openapi_client.rest import ApiException

class TestNotifications(unittest.TestCase):
    """Notifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Notifications
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.notifications.Notifications()  # noqa: E501
        if include_optional :
            return Notifications(
                id = 56, 
                product = 56, 
                user = 56, 
                product_type_added = [
                    'slack'
                    ], 
                product_added = [
                    'slack'
                    ], 
                engagement_added = [
                    'slack'
                    ], 
                test_added = [
                    'slack'
                    ], 
                scan_added = [
                    'slack'
                    ], 
                jira_update = [
                    'slack'
                    ], 
                upcoming_engagement = [
                    'slack'
                    ], 
                stale_engagement = [
                    'slack'
                    ], 
                auto_close_engagement = [
                    'slack'
                    ], 
                close_engagement = [
                    'slack'
                    ], 
                user_mentioned = [
                    'slack'
                    ], 
                code_review = [
                    'slack'
                    ], 
                review_requested = [
                    'slack'
                    ], 
                other = [
                    'slack'
                    ], 
                sla_breach = [
                    'slack'
                    ], 
                risk_acceptance_expiration = [
                    'slack'
                    ], 
                template = True
            )
        else :
            return Notifications(
        )

    def testNotifications(self):
        """Test Notifications"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
