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
from openapi_client.models.finding_to_notes import FindingToNotes  # noqa: E501
from openapi_client.rest import ApiException

class TestFindingToNotes(unittest.TestCase):
    """FindingToNotes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindingToNotes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.finding_to_notes.FindingToNotes()  # noqa: E501
        if include_optional :
            return FindingToNotes(
                finding_id = 56, 
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
                    ]
            )
        else :
            return FindingToNotes(
                finding_id = 56,
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
        )

    def testFindingToNotes(self):
        """Test FindingToNotes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
