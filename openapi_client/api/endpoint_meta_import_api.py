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


class EndpointMetaImportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def endpoint_meta_import_create(self, file, **kwargs):  # noqa: E501
        """Imports a CSV file into a product to propogate arbitrary meta and tags on endpoints.  # noqa: E501

        By Names: - Provide `product_name` of existing product  By ID: - Provide the id of the product in the `product` parameter  In this scenario Defect Dojo will look up the product by the provided details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_meta_import_create(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: (required)
        :param bool create_endpoints:
        :param bool create_tags:
        :param bool create_dojo_meta:
        :param str product_name:
        :param int product:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EndpointMetaImporter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.endpoint_meta_import_create_with_http_info(file, **kwargs)  # noqa: E501

    def endpoint_meta_import_create_with_http_info(self, file, **kwargs):  # noqa: E501
        """Imports a CSV file into a product to propogate arbitrary meta and tags on endpoints.  # noqa: E501

        By Names: - Provide `product_name` of existing product  By ID: - Provide the id of the product in the `product` parameter  In this scenario Defect Dojo will look up the product by the provided details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_meta_import_create_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: (required)
        :param bool create_endpoints:
        :param bool create_tags:
        :param bool create_dojo_meta:
        :param str product_name:
        :param int product:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EndpointMetaImporter, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'file',
            'create_endpoints',
            'create_tags',
            'create_dojo_meta',
            'product_name',
            'product'
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
                    " to method endpoint_meta_import_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `endpoint_meta_import_create`")  # noqa: E501

        if self.api_client.client_side_validation and ('product_name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['product_name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `product_name` when calling `endpoint_meta_import_create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'create_endpoints' in local_var_params:
            form_params.append(('create_endpoints', local_var_params['create_endpoints']))  # noqa: E501
        if 'create_tags' in local_var_params:
            form_params.append(('create_tags', local_var_params['create_tags']))  # noqa: E501
        if 'create_dojo_meta' in local_var_params:
            form_params.append(('create_dojo_meta', local_var_params['create_dojo_meta']))  # noqa: E501
        if 'product_name' in local_var_params:
            form_params.append(('product_name', local_var_params['product_name']))  # noqa: E501
        if 'product' in local_var_params:
            form_params.append(('product', local_var_params['product']))  # noqa: E501

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
            '/endpoint_meta_import/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EndpointMetaImporter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
