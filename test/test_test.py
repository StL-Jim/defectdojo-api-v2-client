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
from openapi_client.models.test import Test  # noqa: E501
from openapi_client.rest import ApiException

class TestTest(unittest.TestCase):
    """Test unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Test
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.test.Test()  # noqa: E501
        if include_optional :
            return Test(
                id = 56, 
                tags = [
                    '0'
                    ], 
                test_type_name = '0', 
                finding_groups = [
                    openapi_client.models.finding_group.FindingGroup(
                        id = 56, 
                        name = '0', 
                        test = 56, 
                        jira_issue = openapi_client.models.jira_issue.JIRAIssue(
                            id = 56, 
                            url = '0', 
                            jira_id = '0', 
                            jira_key = '0', 
                            jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            jira_project = 56, 
                            finding = 56, 
                            engagement = 56, 
                            finding_group = 56, ), )
                    ], 
                scan_type = '0', 
                title = '0', 
                description = '0', 
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                estimated_time = '0', 
                actual_time = '0', 
                percent_complete = -2147483648, 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                version = '0', 
                build_id = '0', 
                commit_hash = '0', 
                branch_tag = '0', 
                engagement = 56, 
                lead = 56, 
                test_type = 56, 
                environment = 56, 
                api_scan_configuration = 56, 
                notes = [
                    openapi_client.models.note.Note(
                        id = 56, 
                        author = openapi_client.models.user_stub.UserStub(
                            id = 56, 
                            username = 'a', 
                            first_name = '0', 
                            last_name = '0', ), 
                        editor = openapi_client.models.user_stub.UserStub(
                            id = 56, 
                            username = 'a', 
                            first_name = '0', 
                            last_name = '0', ), 
                        history = [
                            openapi_client.models.note_history.NoteHistory(
                                id = 56, 
                                current_editor = openapi_client.models.user_stub.UserStub(
                                    id = 56, 
                                    username = 'a', 
                                    first_name = '0', 
                                    last_name = '0', ), 
                                data = '0', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                note_type = 56, )
                            ], 
                        entry = '0', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        private = True, 
                        edited = True, 
                        edit_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        note_type = 56, )
                    ], 
                files = [
                    openapi_client.models.file.File(
                        id = 56, 
                        file = '0', 
                        title = '0', )
                    ]
            )
        else :
            return Test(
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                test_type = 56,
        )

    def testTest(self):
        """Test Test"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()