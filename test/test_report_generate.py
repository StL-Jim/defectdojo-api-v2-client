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
from openapi_client.models.report_generate import ReportGenerate  # noqa: E501
from openapi_client.rest import ApiException

class TestReportGenerate(unittest.TestCase):
    """ReportGenerate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportGenerate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.report_generate.ReportGenerate()  # noqa: E501
        if include_optional :
            return ReportGenerate(
                executive_summary = openapi_client.models.executive_summary.ExecutiveSummary(
                    engagement_name = '0', 
                    engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    test_type_name = '0', 
                    test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_environment_name = '0', 
                    test_strategy_ref = '0', 
                    total_findings = 56, ), 
                product_type = openapi_client.models.product_type.ProductType(
                    id = 56, 
                    name = '0', 
                    description = '0', 
                    critical_product = True, 
                    key_product = True, 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    members = [
                        56
                        ], 
                    authorization_groups = [
                        56
                        ], ), 
                product = openapi_client.models.product.Product(
                    id = 56, 
                    findings_count = 56, 
                    findings_list = [
                        56
                        ], 
                    tags = [
                        '0'
                        ], 
                    product_meta = [
                        openapi_client.models.product_meta.ProductMeta(
                            name = '0', 
                            value = '0', )
                        ], 
                    name = '0', 
                    description = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    prod_numeric_grade = -2147483648, 
                    business_criticality = 'very high', 
                    platform = 'web service', 
                    lifecycle = 'construction', 
                    origin = 'third party library', 
                    user_records = 0, 
                    revenue = '0', 
                    external_audience = True, 
                    internet_accessible = True, 
                    enable_simple_risk_acceptance = True, 
                    enable_full_risk_acceptance = True, 
                    product_manager = 56, 
                    technical_contact = 56, 
                    team_manager = 56, 
                    prod_type = 56, 
                    members = [
                        56
                        ], 
                    authorization_groups = [
                        56
                        ], 
                    regulations = [
                        56
                        ], ), 
                engagement = openapi_client.models.engagement.Engagement(
                    id = 56, 
                    tags = [
                        '0'
                        ], 
                    name = '0', 
                    description = '0', 
                    version = '0', 
                    first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    reason = '0', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    active = True, 
                    tracker = '0', 
                    test_strategy = '0', 
                    threat_model = True, 
                    api_test = True, 
                    pen_test = True, 
                    check_list = True, 
                    status = 'Not Started', 
                    progress = '0', 
                    tmodel_path = '0', 
                    done_testing = True, 
                    engagement_type = 'Interactive', 
                    build_id = '0', 
                    commit_hash = '0', 
                    branch_tag = '0', 
                    source_code_management_uri = '0', 
                    deduplication_on_engagement = True, 
                    lead = 56, 
                    requester = 56, 
                    preset = 56, 
                    report_type = 56, 
                    product = 56, 
                    build_server = 56, 
                    source_code_management_server = 56, 
                    orchestration_engine = 56, 
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
                        ], 
                    risk_acceptance = [
                        56
                        ], ), 
                report_name = '0', 
                report_info = '0', 
                test = openapi_client.models.test.Test(
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
                        ], ), 
                endpoint = openapi_client.models.endpoint.Endpoint(
                    id = 56, 
                    tags = [
                        '0'
                        ], 
                    protocol = '0', 
                    userinfo = '0', 
                    host = '0', 
                    port = -2147483648, 
                    path = '0', 
                    query = '0', 
                    fragment = '0', 
                    product = 56, 
                    endpoint_params = [
                        56
                        ], 
                    endpoint_status = [
                        56
                        ], ), 
                endpoints = [
                    openapi_client.models.endpoint.Endpoint(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        protocol = '0', 
                        userinfo = '0', 
                        host = '0', 
                        port = -2147483648, 
                        path = '0', 
                        query = '0', 
                        fragment = '0', 
                        product = 56, 
                        endpoint_params = [
                            56
                            ], 
                        endpoint_status = [
                            56
                            ], )
                    ], 
                findings = [
                    openapi_client.models.finding.Finding(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        request_response = openapi_client.models.burp_raw_request_response.BurpRawRequestResponse(
                            req_resp = [
                                {
                                    'key' : '0'
                                    }
                                ], ), 
                        accepted_risks = [
                            openapi_client.models.risk_acceptance.RiskAcceptance(
                                id = 56, 
                                name = '0', 
                                recommendation = 'A', 
                                recommendation_details = '0', 
                                decision = 'A', 
                                decision_details = '0', 
                                accepted_by = '0', 
                                path = '0', 
                                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_date_warned = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_date_handled = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                reactivate_expired = True, 
                                restart_sla_expired = True, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                owner = 56, 
                                accepted_findings = [
                                    56
                                    ], 
                                notes = [
                                    56
                                    ], )
                            ], 
                        push_to_jira = True, 
                        age = 56, 
                        sla_days_remaining = 56, 
                        finding_meta = [
                            openapi_client.models.finding_meta.FindingMeta(
                                name = '0', 
                                value = '0', )
                            ], 
                        related_fields = openapi_client.models.finding_related_fields.FindingRelatedFields(
                            test = openapi_client.models.finding_test.FindingTest(
                                id = 56, 
                                title = '0', 
                                test_type = openapi_client.models.finding_test_type.FindingTestType(
                                    id = 56, 
                                    name = '0', ), 
                                engagement = openapi_client.models.finding_engagement.FindingEngagement(
                                    id = 56, 
                                    name = '0', 
                                    product = openapi_client.models.finding_product.FindingProduct(
                                        id = 56, 
                                        name = '0', 
                                        prod_type = openapi_client.models.finding_prod_type.FindingProdType(
                                            id = 56, 
                                            name = '0', ), ), 
                                    branch_tag = '0', 
                                    build_id = '0', 
                                    commit_hash = '0', 
                                    version = '0', ), 
                                environment = openapi_client.models.finding_environment.FindingEnvironment(
                                    id = 56, 
                                    name = '0', ), 
                                branch_tag = '0', 
                                build_id = '0', 
                                commit_hash = '0', 
                                version = '0', ), 
                            jira = openapi_client.models.jira_issue.JIRAIssue(
                                id = 56, 
                                url = '0', 
                                jira_id = '0', 
                                jira_key = '0', 
                                jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                jira_project = 56, 
                                finding = 56, 
                                finding_group = 56, ), ), 
                        jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        display_status = '0', 
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
                                    finding_group = 56, ), )
                            ], 
                        title = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        sla_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        cwe = -2147483648, 
                        cve = 'a', 
                        cvssv3 = 'a', 
                        cvssv3_score = 1.337, 
                        url = '0', 
                        severity = '0', 
                        description = '0', 
                        mitigation = '0', 
                        impact = '0', 
                        steps_to_reproduce = '0', 
                        severity_justification = '0', 
                        references = '0', 
                        active = True, 
                        verified = True, 
                        false_p = True, 
                        duplicate = True, 
                        out_of_scope = True, 
                        risk_accepted = True, 
                        under_review = True, 
                        last_status_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        under_defect_review = True, 
                        is_mitigated = True, 
                        thread_id = 56, 
                        mitigated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        numerical_severity = '0', 
                        last_reviewed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        param = '0', 
                        payload = '0', 
                        hash_code = '0', 
                        line = -2147483648, 
                        file_path = '0', 
                        component_name = '0', 
                        component_version = '0', 
                        static_finding = True, 
                        dynamic_finding = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scanner_confidence = 56, 
                        unique_id_from_tool = '0', 
                        vuln_id_from_tool = '0', 
                        sast_source_object = '0', 
                        sast_sink_object = '0', 
                        sast_source_line = -2147483648, 
                        sast_source_file_path = '0', 
                        nb_occurences = -2147483648, 
                        publish_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        service = '0', 
                        test = 56, 
                        duplicate_finding = 56, 
                        review_requested_by = 56, 
                        defect_review_requested_by = 56, 
                        mitigated_by = 56, 
                        reporter = 56, 
                        last_reviewed_by = 56, 
                        sonarqube_issue = 56, 
                        endpoints = [
                            56
                            ], 
                        endpoint_status = [
                            56
                            ], 
                        reviewers = [
                            56
                            ], 
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
                            56
                            ], 
                        found_by = [
                            56
                            ], )
                    ], 
                user = openapi_client.models.user_stub.UserStub(
                    id = 56, 
                    username = 'a', 
                    first_name = '0', 
                    last_name = '0', ), 
                team_name = '0', 
                title = '0', 
                user_id = 56, 
                host = '0', 
                finding_notes = [
                    openapi_client.models.finding_to_notes.FindingToNotes(
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
                            ], )
                    ]
            )
        else :
            return ReportGenerate(
                executive_summary = openapi_client.models.executive_summary.ExecutiveSummary(
                    engagement_name = '0', 
                    engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    test_type_name = '0', 
                    test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_environment_name = '0', 
                    test_strategy_ref = '0', 
                    total_findings = 56, ),
                report_name = '0',
                report_info = '0',
                team_name = '0',
                title = '0',
                user_id = 56,
                host = '0',
        )

    def testReportGenerate(self):
        """Test ReportGenerate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()