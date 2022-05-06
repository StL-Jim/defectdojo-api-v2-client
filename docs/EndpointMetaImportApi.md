# openapi_client.EndpointMetaImportApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_meta_import_create**](EndpointMetaImportApi.md#endpoint_meta_import_create) | **POST** /endpoint_meta_import/ | Imports a CSV file into a product to propogate arbitrary meta and tags on endpoints.


# **endpoint_meta_import_create**
> EndpointMetaImporter endpoint_meta_import_create(file, create_endpoints=create_endpoints, create_tags=create_tags, create_dojo_meta=create_dojo_meta, product_name=product_name, product=product)

Imports a CSV file into a product to propogate arbitrary meta and tags on endpoints.

By Names: - Provide `product_name` of existing product  By ID: - Provide the id of the product in the `product` parameter  In this scenario Defect Dojo will look up the product by the provided details.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://demo.defectdojo.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://demo.defectdojo.org/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = openapi_client.Configuration(
    host = "https://demo.defectdojo.org/api/v2",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointMetaImportApi(api_client)
    file = '/path/to/file' # file | 
create_endpoints = True # bool |  (optional) (default to True)
create_tags = True # bool |  (optional) (default to True)
create_dojo_meta = False # bool |  (optional) (default to False)
product_name = 'product_name_example' # str |  (optional)
product = 56 # int |  (optional)

    try:
        # Imports a CSV file into a product to propogate arbitrary meta and tags on endpoints.
        api_response = api_instance.endpoint_meta_import_create(file, create_endpoints=create_endpoints, create_tags=create_tags, create_dojo_meta=create_dojo_meta, product_name=product_name, product=product)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndpointMetaImportApi->endpoint_meta_import_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 
 **create_endpoints** | **bool**|  | [optional] [default to True]
 **create_tags** | **bool**|  | [optional] [default to True]
 **create_dojo_meta** | **bool**|  | [optional] [default to False]
 **product_name** | **str**|  | [optional] 
 **product** | **int**|  | [optional] 

### Return type

[**EndpointMetaImporter**](EndpointMetaImporter.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

