# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ImportScanApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def import_scan_create(self, scan_type, **kwargs):  # noqa: E501
        """Imports a scan report into an engagement or product.  # noqa: E501

        By ID: - Create a Product (or use an existing product) - Create an Engagement inside the product - Provide the id of the engagement in the `engagement` parameter  In this scenario a new Test will be created inside the engagement.  By Names: - Create a Product (or use an existing product) - Create an Engagement inside the product - Provide `product_name` - Provide `engagement_name` - Optionally provide `product_type_name`  In this scenario Defect Dojo will look up the Engagement by the provided details.  When using names you can let the importer automatically create Engagements, Products and Product_Types by using `auto_create_context=True`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_scan_create(scan_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scan_type: (required)
        :param date scan_date:
        :param str minimum_severity:
        :param bool active:
        :param bool verified:
        :param int endpoint_to_add:
        :param file file:
        :param str product_type_name:
        :param str product_name:
        :param str engagement_name:
        :param int engagement:
        :param str test_title:
        :param bool auto_create_context:
        :param int lead:
        :param list[str] tags:
        :param bool close_old_findings: Select if old findings no longer present in the report get closed as mitigated when importing. If service has been set, only the findings for this service will be closed.
        :param bool push_to_jira:
        :param str environment:
        :param str version:
        :param str build_id:
        :param str branch_tag:
        :param str commit_hash:
        :param int api_scan_configuration:
        :param str service: A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope.
        :param str group_by: Choose an option to automatically group new findings by the chosen option.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ImportScan
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.import_scan_create_with_http_info(scan_type, **kwargs)  # noqa: E501

    def import_scan_create_with_http_info(self, scan_type, **kwargs):  # noqa: E501
        """Imports a scan report into an engagement or product.  # noqa: E501

        By ID: - Create a Product (or use an existing product) - Create an Engagement inside the product - Provide the id of the engagement in the `engagement` parameter  In this scenario a new Test will be created inside the engagement.  By Names: - Create a Product (or use an existing product) - Create an Engagement inside the product - Provide `product_name` - Provide `engagement_name` - Optionally provide `product_type_name`  In this scenario Defect Dojo will look up the Engagement by the provided details.  When using names you can let the importer automatically create Engagements, Products and Product_Types by using `auto_create_context=True`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_scan_create_with_http_info(scan_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scan_type: (required)
        :param date scan_date:
        :param str minimum_severity:
        :param bool active:
        :param bool verified:
        :param int endpoint_to_add:
        :param file file:
        :param str product_type_name:
        :param str product_name:
        :param str engagement_name:
        :param int engagement:
        :param str test_title:
        :param bool auto_create_context:
        :param int lead:
        :param list[str] tags:
        :param bool close_old_findings: Select if old findings no longer present in the report get closed as mitigated when importing. If service has been set, only the findings for this service will be closed.
        :param bool push_to_jira:
        :param str environment:
        :param str version:
        :param str build_id:
        :param str branch_tag:
        :param str commit_hash:
        :param int api_scan_configuration:
        :param str service: A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope.
        :param str group_by: Choose an option to automatically group new findings by the chosen option.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ImportScan, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'scan_type',
            'scan_date',
            'minimum_severity',
            'active',
            'verified',
            'endpoint_to_add',
            'file',
            'product_type_name',
            'product_name',
            'engagement_name',
            'engagement',
            'test_title',
            'auto_create_context',
            'lead',
            'tags',
            'close_old_findings',
            'push_to_jira',
            'environment',
            'version',
            'build_id',
            'branch_tag',
            'commit_hash',
            'api_scan_configuration',
            'service',
            'group_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_scan_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scan_type' is set
        if self.api_client.client_side_validation and ('scan_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['scan_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scan_type` when calling `import_scan_create`")  # noqa: E501

        if self.api_client.client_side_validation and ('product_type_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['product_type_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `product_type_name` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('product_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['product_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `product_name` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('engagement_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['engagement_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `engagement_name` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('test_title' in local_var_params and  # noqa: E501
                                                        len(local_var_params['test_title']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `test_title` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('tags' in local_var_params and  # noqa: E501
                                                        len(local_var_params['tags']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `tags` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('environment' in local_var_params and  # noqa: E501
                                                        len(local_var_params['environment']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `environment` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `version` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('build_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['build_id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `build_id` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('branch_tag' in local_var_params and  # noqa: E501
                                                        len(local_var_params['branch_tag']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `branch_tag` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('commit_hash' in local_var_params and  # noqa: E501
                                                        len(local_var_params['commit_hash']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `commit_hash` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('service' in local_var_params and  # noqa: E501
                                                        len(local_var_params['service']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `service` when calling `import_scan_create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'scan_date' in local_var_params:
            form_params.append(('scan_date', local_var_params['scan_date']))  # noqa: E501
        if 'minimum_severity' in local_var_params:
            form_params.append(('minimum_severity', local_var_params['minimum_severity']))  # noqa: E501
        if 'active' in local_var_params:
            form_params.append(('active', local_var_params['active']))  # noqa: E501
        if 'verified' in local_var_params:
            form_params.append(('verified', local_var_params['verified']))  # noqa: E501
        if 'scan_type' in local_var_params:
            form_params.append(('scan_type', local_var_params['scan_type']))  # noqa: E501
        if 'endpoint_to_add' in local_var_params:
            form_params.append(('endpoint_to_add', local_var_params['endpoint_to_add']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'product_type_name' in local_var_params:
            form_params.append(('product_type_name', local_var_params['product_type_name']))  # noqa: E501
        if 'product_name' in local_var_params:
            form_params.append(('product_name', local_var_params['product_name']))  # noqa: E501
        if 'engagement_name' in local_var_params:
            form_params.append(('engagement_name', local_var_params['engagement_name']))  # noqa: E501
        if 'engagement' in local_var_params:
            form_params.append(('engagement', local_var_params['engagement']))  # noqa: E501
        if 'test_title' in local_var_params:
            form_params.append(('test_title', local_var_params['test_title']))  # noqa: E501
        if 'auto_create_context' in local_var_params:
            form_params.append(('auto_create_context', local_var_params['auto_create_context']))  # noqa: E501
        if 'lead' in local_var_params:
            form_params.append(('lead', local_var_params['lead']))  # noqa: E501
        if 'tags' in local_var_params:
            form_params.append(('tags', local_var_params['tags']))  # noqa: E501
            collection_formats['tags'] = 'csv'  # noqa: E501
        if 'close_old_findings' in local_var_params:
            form_params.append(('close_old_findings', local_var_params['close_old_findings']))  # noqa: E501
        if 'push_to_jira' in local_var_params:
            form_params.append(('push_to_jira', local_var_params['push_to_jira']))  # noqa: E501
        if 'environment' in local_var_params:
            form_params.append(('environment', local_var_params['environment']))  # noqa: E501
        if 'version' in local_var_params:
            form_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'build_id' in local_var_params:
            form_params.append(('build_id', local_var_params['build_id']))  # noqa: E501
        if 'branch_tag' in local_var_params:
            form_params.append(('branch_tag', local_var_params['branch_tag']))  # noqa: E501
        if 'commit_hash' in local_var_params:
            form_params.append(('commit_hash', local_var_params['commit_hash']))  # noqa: E501
        if 'api_scan_configuration' in local_var_params:
            form_params.append(('api_scan_configuration', local_var_params['api_scan_configuration']))  # noqa: E501
        if 'service' in local_var_params:
            form_params.append(('service', local_var_params['service']))  # noqa: E501
        if 'group_by' in local_var_params:
            form_params.append(('group_by', local_var_params['group_by']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/import-scan/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImportScan',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
