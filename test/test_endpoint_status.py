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
from openapi_client.models.endpoint_status import EndpointStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestEndpointStatus(unittest.TestCase):
    """EndpointStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EndpointStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.endpoint_status.EndpointStatus()  # noqa: E501
        if include_optional :
            return EndpointStatus(
                id = 56, 
                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                mitigated = True, 
                mitigated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                false_positive = True, 
                out_of_scope = True, 
                risk_accepted = True, 
                mitigated_by = 56, 
                endpoint = 56, 
                finding = 56
            )
        else :
            return EndpointStatus(
        )

    def testEndpointStatus(self):
        """Test EndpointStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
