# openapi_client.ProductsApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_create**](ProductsApi.md#products_create) | **POST** /products/ | 
[**products_delete**](ProductsApi.md#products_delete) | **DELETE** /products/{id}/ | 
[**products_generate_report**](ProductsApi.md#products_generate_report) | **POST** /products/{id}/generate_report/ | 
[**products_list**](ProductsApi.md#products_list) | **GET** /products/ | 
[**products_partial_update**](ProductsApi.md#products_partial_update) | **PATCH** /products/{id}/ | 
[**products_read**](ProductsApi.md#products_read) | **GET** /products/{id}/ | 
[**products_update**](ProductsApi.md#products_update) | **PUT** /products/{id}/ | 


# **products_create**
> Product products_create(data)



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
    api_instance = openapi_client.ProductsApi(api_client)
    data = openapi_client.Product() # Product | 

    try:
        api_response = api_instance.products_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_delete**
> products_delete(id)



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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.

    try:
        api_instance.products_delete(id)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_generate_report**
> ReportGenerate products_generate_report(id, data)



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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
data = openapi_client.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.products_generate_report(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**ReportGenerateOption**](ReportGenerateOption.md)|  | 

### Return type

[**ReportGenerate**](ReportGenerate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_list**
> InlineResponse20038 products_list(external_audience=external_audience, internet_accessible=internet_accessible, name=name, description=description, business_criticality=business_criticality, platform=platform, lifecycle=lifecycle, origin=origin, id=id, product_manager=product_manager, technical_contact=technical_contact, team_manager=team_manager, prod_type=prod_type, tid=tid, prod_numeric_grade=prod_numeric_grade, user_records=user_records, regulations=regulations, tag=tag, tags=tags, not_tag=not_tag, not_tags=not_tags, created=created, updated=updated, revenue=revenue, o=o, limit=limit, offset=offset, prefetch=prefetch)



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
    api_instance = openapi_client.ProductsApi(api_client)
    external_audience = 'external_audience_example' # str | Filter the returned list by external_audience (optional)
internet_accessible = 'internet_accessible_example' # str | Filter the returned list by internet_accessible (optional)
name = 'name_example' # str | Filter the returned list by name (optional)
description = 'description_example' # str | Filter the returned list by description (optional)
business_criticality = 'business_criticality_example' # str | Filter the returned list by business_criticality (optional)
platform = 'platform_example' # str | Filter the returned list by platform (optional)
lifecycle = 'lifecycle_example' # str | Filter the returned list by lifecycle (optional)
origin = 'origin_example' # str | Filter the returned list by origin (optional)
id = 3.4 # float | Multiple values may be separated by commas. (optional)
product_manager = 3.4 # float | Multiple values may be separated by commas. (optional)
technical_contact = 3.4 # float | Multiple values may be separated by commas. (optional)
team_manager = 3.4 # float | Multiple values may be separated by commas. (optional)
prod_type = 3.4 # float | Multiple values may be separated by commas. (optional)
tid = 3.4 # float | Multiple values may be separated by commas. (optional)
prod_numeric_grade = 3.4 # float | Multiple values may be separated by commas. (optional)
user_records = 3.4 # float | Multiple values may be separated by commas. (optional)
regulations = 3.4 # float | Multiple values may be separated by commas. (optional)
tag = 'tag_example' # str | Filter the returned list by tag (optional)
tags = 'tags_example' # str | Comma seperated list of exact tags (optional)
not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
not_tags = 'not_tags_example' # str | Comma seperated list of exact tags not present on product (optional)
created = 'created_example' # str | Filter the returned list by created (optional)
updated = 'updated_example' # str | Filter the returned list by updated (optional)
revenue = 3.4 # float | Filter the returned list by revenue (optional)
o = 'o_example' # str | Filter the returned list by o (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
prefetch = ['prefetch_example'] # list[str] |  (optional)

    try:
        api_response = api_instance.products_list(external_audience=external_audience, internet_accessible=internet_accessible, name=name, description=description, business_criticality=business_criticality, platform=platform, lifecycle=lifecycle, origin=origin, id=id, product_manager=product_manager, technical_contact=technical_contact, team_manager=team_manager, prod_type=prod_type, tid=tid, prod_numeric_grade=prod_numeric_grade, user_records=user_records, regulations=regulations, tag=tag, tags=tags, not_tag=not_tag, not_tags=not_tags, created=created, updated=updated, revenue=revenue, o=o, limit=limit, offset=offset, prefetch=prefetch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_audience** | **str**| Filter the returned list by external_audience | [optional] 
 **internet_accessible** | **str**| Filter the returned list by internet_accessible | [optional] 
 **name** | **str**| Filter the returned list by name | [optional] 
 **description** | **str**| Filter the returned list by description | [optional] 
 **business_criticality** | **str**| Filter the returned list by business_criticality | [optional] 
 **platform** | **str**| Filter the returned list by platform | [optional] 
 **lifecycle** | **str**| Filter the returned list by lifecycle | [optional] 
 **origin** | **str**| Filter the returned list by origin | [optional] 
 **id** | **float**| Multiple values may be separated by commas. | [optional] 
 **product_manager** | **float**| Multiple values may be separated by commas. | [optional] 
 **technical_contact** | **float**| Multiple values may be separated by commas. | [optional] 
 **team_manager** | **float**| Multiple values may be separated by commas. | [optional] 
 **prod_type** | **float**| Multiple values may be separated by commas. | [optional] 
 **tid** | **float**| Multiple values may be separated by commas. | [optional] 
 **prod_numeric_grade** | **float**| Multiple values may be separated by commas. | [optional] 
 **user_records** | **float**| Multiple values may be separated by commas. | [optional] 
 **regulations** | **float**| Multiple values may be separated by commas. | [optional] 
 **tag** | **str**| Filter the returned list by tag | [optional] 
 **tags** | **str**| Comma seperated list of exact tags | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | **str**| Comma seperated list of exact tags not present on product | [optional] 
 **created** | **str**| Filter the returned list by created | [optional] 
 **updated** | **str**| Filter the returned list by updated | [optional] 
 **revenue** | **float**| Filter the returned list by revenue | [optional] 
 **o** | **str**| Filter the returned list by o | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_partial_update**
> Product products_partial_update(id, data)



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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
data = openapi_client.Product() # Product | 

    try:
        api_response = api_instance.products_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_read**
> InlineResponse20039 products_read(id, prefetch=prefetch)



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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
prefetch = ['prefetch_example'] # list[str] |  (optional)

    try:
        api_response = api_instance.products_read(id, prefetch=prefetch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update**
> Product products_update(id, data)



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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
data = openapi_client.Product() # Product | 

    try:
        api_response = api_instance.products_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->products_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

