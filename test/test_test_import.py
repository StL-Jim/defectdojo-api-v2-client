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
from openapi_client.models.test_import import TestImport  # noqa: E501
from openapi_client.rest import ApiException

class TestTestImport(unittest.TestCase):
    """TestImport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestImport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.test_import.TestImport()  # noqa: E501
        if include_optional :
            return TestImport(
                id = 56, 
                test_import_finding_action_set = [
                    openapi_client.models.test_import_finding_action.TestImportFindingAction(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        action = 'N', 
                        test_import = 56, 
                        finding = 56, )
                    ], 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                import_settings = openapi_client.models.import_settings.Import settings(), 
                type = '0', 
                version = '0', 
                build_id = '0', 
                commit_hash = '0', 
                branch_tag = '0', 
                test = 56, 
                findings_affected = [
                    56
                    ]
            )
        else :
            return TestImport(
        )

    def testTestImport(self):
        """Test TestImport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()