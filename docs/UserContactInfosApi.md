# openapi_client.UserContactInfosApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_contact_infos_create**](UserContactInfosApi.md#user_contact_infos_create) | **POST** /user_contact_infos/ | 
[**user_contact_infos_delete**](UserContactInfosApi.md#user_contact_infos_delete) | **DELETE** /user_contact_infos/{id}/ | 
[**user_contact_infos_list**](UserContactInfosApi.md#user_contact_infos_list) | **GET** /user_contact_infos/ | 
[**user_contact_infos_partial_update**](UserContactInfosApi.md#user_contact_infos_partial_update) | **PATCH** /user_contact_infos/{id}/ | 
[**user_contact_infos_read**](UserContactInfosApi.md#user_contact_infos_read) | **GET** /user_contact_infos/{id}/ | 
[**user_contact_infos_update**](UserContactInfosApi.md#user_contact_infos_update) | **PUT** /user_contact_infos/{id}/ | 


# **user_contact_infos_create**
> UserContactInfo user_contact_infos_create(data)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    data = openapi_client.UserContactInfo() # UserContactInfo | 

    try:
        api_response = api_instance.user_contact_infos_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserContactInfo**](UserContactInfo.md)|  | 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

# **user_contact_infos_delete**
> user_contact_infos_delete(id)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.

    try:
        api_instance.user_contact_infos_delete(id)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 

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

# **user_contact_infos_list**
> InlineResponse20054 user_contact_infos_list(user=user, title=title, phone_number=phone_number, cell_number=cell_number, twitter_username=twitter_username, github_username=github_username, slack_username=slack_username, slack_user_id=slack_user_id, block_execution=block_execution, force_password_reset=force_password_reset, limit=limit, offset=offset, prefetch=prefetch)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    user = 'user_example' # str |  (optional)
title = 'title_example' # str |  (optional)
phone_number = 'phone_number_example' # str |  (optional)
cell_number = 'cell_number_example' # str |  (optional)
twitter_username = 'twitter_username_example' # str |  (optional)
github_username = 'github_username_example' # str |  (optional)
slack_username = 'slack_username_example' # str |  (optional)
slack_user_id = 'slack_user_id_example' # str |  (optional)
block_execution = 'block_execution_example' # str |  (optional)
force_password_reset = 'force_password_reset_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
prefetch = ['prefetch_example'] # list[str] |  (optional)

    try:
        api_response = api_instance.user_contact_infos_list(user=user, title=title, phone_number=phone_number, cell_number=cell_number, twitter_username=twitter_username, github_username=github_username, slack_username=slack_username, slack_user_id=slack_user_id, block_execution=block_execution, force_password_reset=force_password_reset, limit=limit, offset=offset, prefetch=prefetch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **phone_number** | **str**|  | [optional] 
 **cell_number** | **str**|  | [optional] 
 **twitter_username** | **str**|  | [optional] 
 **github_username** | **str**|  | [optional] 
 **slack_username** | **str**|  | [optional] 
 **slack_user_id** | **str**|  | [optional] 
 **block_execution** | **str**|  | [optional] 
 **force_password_reset** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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

# **user_contact_infos_partial_update**
> UserContactInfo user_contact_infos_partial_update(id, data)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
data = openapi_client.UserContactInfo() # UserContactInfo | 

    try:
        api_response = api_instance.user_contact_infos_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **data** | [**UserContactInfo**](UserContactInfo.md)|  | 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

# **user_contact_infos_read**
> InlineResponse20055 user_contact_infos_read(id, prefetch=prefetch)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
prefetch = ['prefetch_example'] # list[str] |  (optional)

    try:
        api_response = api_instance.user_contact_infos_read(id, prefetch=prefetch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

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

# **user_contact_infos_update**
> UserContactInfo user_contact_infos_update(id, data)



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
    api_instance = openapi_client.UserContactInfosApi(api_client)
    id = 56 # int | A unique integer value identifying this user contact info.
data = openapi_client.UserContactInfo() # UserContactInfo | 

    try:
        api_response = api_instance.user_contact_infos_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserContactInfosApi->user_contact_infos_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user contact info. | 
 **data** | [**UserContactInfo**](UserContactInfo.md)|  | 

### Return type

[**UserContactInfo**](UserContactInfo.md)

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

