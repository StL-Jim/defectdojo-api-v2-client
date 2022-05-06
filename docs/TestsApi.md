# openapi_client.TestsApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tests_accept_risks**](TestsApi.md#tests_accept_risks) | **POST** /tests/{id}/accept_risks/ | 
[**tests_create**](TestsApi.md#tests_create) | **POST** /tests/ | 
[**tests_delete**](TestsApi.md#tests_delete) | **DELETE** /tests/{id}/ | 
[**tests_files_create**](TestsApi.md#tests_files_create) | **POST** /tests/{id}/files/ | 
[**tests_files_read**](TestsApi.md#tests_files_read) | **GET** /tests/{id}/files/ | 
[**tests_generate_report**](TestsApi.md#tests_generate_report) | **POST** /tests/{id}/generate_report/ | 
[**tests_list**](TestsApi.md#tests_list) | **GET** /tests/ | 
[**tests_notes_create**](TestsApi.md#tests_notes_create) | **POST** /tests/{id}/notes/ | 
[**tests_notes_read**](TestsApi.md#tests_notes_read) | **GET** /tests/{id}/notes/ | 
[**tests_partial_update**](TestsApi.md#tests_partial_update) | **PATCH** /tests/{id}/ | 
[**tests_read**](TestsApi.md#tests_read) | **GET** /tests/{id}/ | 
[**tests_update**](TestsApi.md#tests_update) | **PUT** /tests/{id}/ | 


# **tests_accept_risks**
> list[RiskAcceptance] tests_accept_risks(id, data)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = [openapi_client.AcceptedRisk()] # list[AcceptedRisk] | 

    try:
        api_response = api_instance.tests_accept_risks(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_accept_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**list[AcceptedRisk]**](AcceptedRisk.md)|  | 

### Return type

[**list[RiskAcceptance]**](RiskAcceptance.md)

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

# **tests_create**
> TestCreate tests_create(data)



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
    api_instance = openapi_client.TestsApi(api_client)
    data = openapi_client.TestCreate() # TestCreate | 

    try:
        api_response = api_instance.tests_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TestCreate**](TestCreate.md)|  | 

### Return type

[**TestCreate**](TestCreate.md)

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

# **tests_delete**
> tests_delete(id)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_instance.tests_delete(id)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

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

# **tests_files_create**
> File tests_files_create(id, title, file)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
title = 'title_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.tests_files_create(id, title, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_files_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **title** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**File**](File.md)

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

# **tests_files_read**
> TestToFiles tests_files_read(id)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.tests_files_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_files_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**TestToFiles**](TestToFiles.md)

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

# **tests_generate_report**
> ReportGenerate tests_generate_report(id, data)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = openapi_client.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.tests_generate_report(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
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

# **tests_list**
> InlineResponse20050 tests_list(id=id, title=title, test_type=test_type, target_start=target_start, target_end=target_end, notes=notes, percent_complete=percent_complete, actual_time=actual_time, engagement=engagement, version=version, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, tag=tag, tags=tags, engagement__tags=engagement__tags, engagement__product__tags__name=engagement__product__tags__name, not_tag=not_tag, not_tags=not_tags, not_engagement__tags=not_engagement__tags, not_engagement__product__tags__name=not_engagement__product__tags__name, o=o, limit=limit, offset=offset)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 3.4 # float |  (optional)
title = 'title_example' # str |  (optional)
test_type = 'test_type_example' # str |  (optional)
target_start = 'target_start_example' # str |  (optional)
target_end = 'target_end_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
percent_complete = 3.4 # float |  (optional)
actual_time = 'actual_time_example' # str |  (optional)
engagement = 'engagement_example' # str |  (optional)
version = 'version_example' # str |  (optional)
branch_tag = 'branch_tag_example' # str |  (optional)
build_id = 'build_id_example' # str |  (optional)
commit_hash = 'commit_hash_example' # str |  (optional)
api_scan_configuration = 'api_scan_configuration_example' # str |  (optional)
tag = 'tag_example' # str | Tag name contains (optional)
tags = 'tags_example' # str | Comma seperated list of exact tags (optional)
engagement__tags = 'engagement__tags_example' # str | Comma seperated list of exact tags present on engagement (optional)
engagement__product__tags__name = 'engagement__product__tags__name_example' # str | Comma seperated list of exact tags present on product (optional)
not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
not_tags = 'not_tags_example' # str | Comma seperated list of exact tags not present on model (optional)
not_engagement__tags = 'not_engagement__tags_example' # str | Comma seperated list of exact tags not present on engagement (optional)
not_engagement__product__tags__name = 'not_engagement__product__tags__name_example' # str | Comma seperated list of exact tags not present on product (optional)
o = 'o_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.tests_list(id=id, title=title, test_type=test_type, target_start=target_start, target_end=target_end, notes=notes, percent_complete=percent_complete, actual_time=actual_time, engagement=engagement, version=version, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, tag=tag, tags=tags, engagement__tags=engagement__tags, engagement__product__tags__name=engagement__product__tags__name, not_tag=not_tag, not_tags=not_tags, not_engagement__tags=not_engagement__tags, not_engagement__product__tags__name=not_engagement__product__tags__name, o=o, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **title** | **str**|  | [optional] 
 **test_type** | **str**|  | [optional] 
 **target_start** | **str**|  | [optional] 
 **target_end** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **percent_complete** | **float**|  | [optional] 
 **actual_time** | **str**|  | [optional] 
 **engagement** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **branch_tag** | **str**|  | [optional] 
 **build_id** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **api_scan_configuration** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **tags** | **str**| Comma seperated list of exact tags | [optional] 
 **engagement__tags** | **str**| Comma seperated list of exact tags present on engagement | [optional] 
 **engagement__product__tags__name** | **str**| Comma seperated list of exact tags present on product | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | **str**| Comma seperated list of exact tags not present on model | [optional] 
 **not_engagement__tags** | **str**| Comma seperated list of exact tags not present on engagement | [optional] 
 **not_engagement__product__tags__name** | **str**| Comma seperated list of exact tags not present on product | [optional] 
 **o** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

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

# **tests_notes_create**
> Note tests_notes_create(id, data)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = openapi_client.AddNewNoteOption() # AddNewNoteOption | 

    try:
        api_response = api_instance.tests_notes_create(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**AddNewNoteOption**](AddNewNoteOption.md)|  | 

### Return type

[**Note**](Note.md)

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

# **tests_notes_read**
> TestToNotes tests_notes_read(id)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.tests_notes_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**TestToNotes**](TestToNotes.md)

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

# **tests_partial_update**
> Test tests_partial_update(id, data)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = openapi_client.Test() # Test | 

    try:
        api_response = api_instance.tests_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**Test**](Test.md)|  | 

### Return type

[**Test**](Test.md)

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

# **tests_read**
> Test tests_read(id)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.tests_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**Test**](Test.md)

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

# **tests_update**
> Test tests_update(id, data)



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
    api_instance = openapi_client.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = openapi_client.Test() # Test | 

    try:
        api_response = api_instance.tests_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**Test**](Test.md)|  | 

### Return type

[**Test**](Test.md)

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

