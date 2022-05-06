# openapi_client.SonarqubeTransitionsApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sonarqube_transitions_create**](SonarqubeTransitionsApi.md#sonarqube_transitions_create) | **POST** /sonarqube_transitions/ | 
[**sonarqube_transitions_delete**](SonarqubeTransitionsApi.md#sonarqube_transitions_delete) | **DELETE** /sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_list**](SonarqubeTransitionsApi.md#sonarqube_transitions_list) | **GET** /sonarqube_transitions/ | 
[**sonarqube_transitions_partial_update**](SonarqubeTransitionsApi.md#sonarqube_transitions_partial_update) | **PATCH** /sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_read**](SonarqubeTransitionsApi.md#sonarqube_transitions_read) | **GET** /sonarqube_transitions/{id}/ | 
[**sonarqube_transitions_update**](SonarqubeTransitionsApi.md#sonarqube_transitions_update) | **PUT** /sonarqube_transitions/{id}/ | 


# **sonarqube_transitions_create**
> SonarqubeIssueTransition sonarqube_transitions_create(data)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    data = openapi_client.SonarqubeIssueTransition() # SonarqubeIssueTransition | 

    try:
        api_response = api_instance.sonarqube_transitions_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)|  | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_delete**
> sonarqube_transitions_delete(id)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.

    try:
        api_instance.sonarqube_transitions_delete(id)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 

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

# **sonarqube_transitions_list**
> InlineResponse20043 sonarqube_transitions_list(id=id, sonarqube_issue=sonarqube_issue, finding_status=finding_status, sonarqube_status=sonarqube_status, transitions=transitions, limit=limit, offset=offset)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    id = 3.4 # float |  (optional)
sonarqube_issue = 'sonarqube_issue_example' # str |  (optional)
finding_status = 'finding_status_example' # str |  (optional)
sonarqube_status = 'sonarqube_status_example' # str |  (optional)
transitions = 'transitions_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.sonarqube_transitions_list(id=id, sonarqube_issue=sonarqube_issue, finding_status=finding_status, sonarqube_status=sonarqube_status, transitions=transitions, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **sonarqube_issue** | **str**|  | [optional] 
 **finding_status** | **str**|  | [optional] 
 **sonarqube_status** | **str**|  | [optional] 
 **transitions** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

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

# **sonarqube_transitions_partial_update**
> SonarqubeIssueTransition sonarqube_transitions_partial_update(id, data)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.
data = openapi_client.SonarqubeIssueTransition() # SonarqubeIssueTransition | 

    try:
        api_response = api_instance.sonarqube_transitions_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 
 **data** | [**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)|  | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_read**
> SonarqubeIssueTransition sonarqube_transitions_read(id)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.

    try:
        api_response = api_instance.sonarqube_transitions_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

# **sonarqube_transitions_update**
> SonarqubeIssueTransition sonarqube_transitions_update(id, data)



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
    api_instance = openapi_client.SonarqubeTransitionsApi(api_client)
    id = 56 # int | A unique integer value identifying this sonarqube_ issue_ transition.
data = openapi_client.SonarqubeIssueTransition() # SonarqubeIssueTransition | 

    try:
        api_response = api_instance.sonarqube_transitions_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SonarqubeTransitionsApi->sonarqube_transitions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sonarqube_ issue_ transition. | 
 **data** | [**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)|  | 

### Return type

[**SonarqubeIssueTransition**](SonarqubeIssueTransition.md)

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

