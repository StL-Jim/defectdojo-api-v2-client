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
from openapi_client.models.inline_response2009 import InlineResponse2009  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2009(unittest.TestCase):
    """InlineResponse2009 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2009
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2009.InlineResponse2009()  # noqa: E501
        if include_optional :
            return InlineResponse2009(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    openapi_client.models.finding_template.FindingTemplate(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        title = '0', 
                        cwe = -2147483648, 
                        cve = 'a', 
                        cvssv3 = 'a', 
                        severity = '0', 
                        description = '0', 
                        mitigation = '0', 
                        impact = '0', 
                        references = '0', 
                        last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        numerical_severity = '0', 
                        template_match = True, 
                        template_match_title = True, )
                    ]
            )
        else :
            return InlineResponse2009(
                count = 56,
                results = [
                    openapi_client.models.finding_template.FindingTemplate(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        title = '0', 
                        cwe = -2147483648, 
                        cve = 'a', 
                        cvssv3 = 'a', 
                        severity = '0', 
                        description = '0', 
                        mitigation = '0', 
                        impact = '0', 
                        references = '0', 
                        last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        numerical_severity = '0', 
                        template_match = True, 
                        template_match_title = True, )
                    ],
        )

    def testInlineResponse2009(self):
        """Test InlineResponse2009"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
