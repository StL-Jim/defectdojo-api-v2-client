# openapi_client.FindingsApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findings_accept_risks**](FindingsApi.md#findings_accept_risks) | **POST** /findings/accept_risks/ | 
[**findings_create**](FindingsApi.md#findings_create) | **POST** /findings/ | 
[**findings_delete**](FindingsApi.md#findings_delete) | **DELETE** /findings/{id}/ | 
[**findings_duplicate_reset_finding_duplicate_status**](FindingsApi.md#findings_duplicate_reset_finding_duplicate_status) | **POST** /findings/{id}/duplicate/reset/ | 
[**findings_files_create**](FindingsApi.md#findings_files_create) | **POST** /findings/{id}/files/ | 
[**findings_files_read**](FindingsApi.md#findings_files_read) | **GET** /findings/{id}/files/ | 
[**findings_generate_report**](FindingsApi.md#findings_generate_report) | **POST** /findings/generate_report/ | 
[**findings_get_duplicate_cluster**](FindingsApi.md#findings_get_duplicate_cluster) | **GET** /findings/{id}/duplicate/ | 
[**findings_list**](FindingsApi.md#findings_list) | **GET** /findings/ | 
[**findings_metadata_create**](FindingsApi.md#findings_metadata_create) | **POST** /findings/{id}/metadata/ | 
[**findings_metadata_delete**](FindingsApi.md#findings_metadata_delete) | **DELETE** /findings/{id}/metadata/ | 
[**findings_metadata_read**](FindingsApi.md#findings_metadata_read) | **GET** /findings/{id}/metadata/ | 
[**findings_metadata_update**](FindingsApi.md#findings_metadata_update) | **PUT** /findings/{id}/metadata/ | 
[**findings_notes_create**](FindingsApi.md#findings_notes_create) | **POST** /findings/{id}/notes/ | 
[**findings_notes_read**](FindingsApi.md#findings_notes_read) | **GET** /findings/{id}/notes/ | 
[**findings_partial_update**](FindingsApi.md#findings_partial_update) | **PATCH** /findings/{id}/ | 
[**findings_read**](FindingsApi.md#findings_read) | **GET** /findings/{id}/ | 
[**findings_remove_note**](FindingsApi.md#findings_remove_note) | **PATCH** /findings/{id}/remove_note/ | 
[**findings_remove_tags_partial_update**](FindingsApi.md#findings_remove_tags_partial_update) | **PATCH** /findings/{id}/remove_tags/ | 
[**findings_remove_tags_update**](FindingsApi.md#findings_remove_tags_update) | **PUT** /findings/{id}/remove_tags/ | 
[**findings_request_response_create**](FindingsApi.md#findings_request_response_create) | **POST** /findings/{id}/request_response/ | 
[**findings_request_response_read**](FindingsApi.md#findings_request_response_read) | **GET** /findings/{id}/request_response/ | 
[**findings_set_finding_as_original**](FindingsApi.md#findings_set_finding_as_original) | **POST** /findings/{id}/original/{new_fid}/ | 
[**findings_tags_create**](FindingsApi.md#findings_tags_create) | **POST** /findings/{id}/tags/ | 
[**findings_tags_read**](FindingsApi.md#findings_tags_read) | **GET** /findings/{id}/tags/ | 
[**findings_update**](FindingsApi.md#findings_update) | **PUT** /findings/{id}/ | 


# **findings_accept_risks**
> list[RiskAcceptance] findings_accept_risks(data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    data = [openapi_client.AcceptedRisk()] # list[AcceptedRisk] | 

    try:
        api_response = api_instance.findings_accept_risks(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_accept_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **findings_create**
> FindingCreate findings_create(data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    data = openapi_client.FindingCreate() # FindingCreate | 

    try:
        api_response = api_instance.findings_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

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

# **findings_delete**
> findings_delete(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_instance.findings_delete(id)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

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

# **findings_duplicate_reset_finding_duplicate_status**
> findings_duplicate_reset_finding_duplicate_status(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_instance.findings_duplicate_reset_finding_duplicate_status(id)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_duplicate_reset_finding_duplicate_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

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

# **findings_files_create**
> File findings_files_create(id, title, file)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
title = 'title_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.findings_files_create(id, title, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_files_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
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

# **findings_files_read**
> FindingToFiles findings_files_read(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_files_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_files_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**FindingToFiles**](FindingToFiles.md)

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

# **findings_generate_report**
> ReportGenerate findings_generate_report(data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    data = openapi_client.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.findings_generate_report(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **findings_get_duplicate_cluster**
> list[Finding] findings_get_duplicate_cluster(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_get_duplicate_cluster(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_get_duplicate_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**list[Finding]**](Finding.md)

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

# **findings_list**
> InlineResponse20010 findings_list(title=title, date=date, sla_start_date=sla_start_date, cwe=cwe, cve=cve, cvssv3=cvssv3, cvssv3_score=cvssv3_score, severity=severity, description=description, mitigation=mitigation, impact=impact, steps_to_reproduce=steps_to_reproduce, severity_justification=severity_justification, endpoints=endpoints, references=references, test=test, active=active, verified=verified, false_p=false_p, duplicate=duplicate, duplicate_finding=duplicate_finding, out_of_scope=out_of_scope, risk_accepted=risk_accepted, under_review=under_review, last_status_update=last_status_update, review_requested_by=review_requested_by, reviewers=reviewers, under_defect_review=under_defect_review, defect_review_requested_by=defect_review_requested_by, is_mitigated=is_mitigated, mitigated=mitigated, mitigated_by=mitigated_by, reporter=reporter, numerical_severity=numerical_severity, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, param=param, payload=payload, hash_code=hash_code, file_path=file_path, component_name=component_name, component_version=component_version, found_by=found_by, static_finding=static_finding, dynamic_finding=dynamic_finding, created=created, scanner_confidence=scanner_confidence, sonarqube_issue=sonarqube_issue, unique_id_from_tool=unique_id_from_tool, vuln_id_from_tool=vuln_id_from_tool, sast_source_object=sast_source_object, sast_sink_object=sast_sink_object, sast_source_line=sast_source_line, sast_source_file_path=sast_source_file_path, nb_occurences=nb_occurences, publish_date=publish_date, service=service, tags=tags, step_to_reproduce=step_to_reproduce, jira_creation=jira_creation, jira_change=jira_change, id=id, test__test_type=test__test_type, test__engagement=test__engagement, test__engagement__product=test__engagement__product, finding_group=finding_group, risk_acceptance=risk_acceptance, tag=tag, test__tags=test__tags, test__engagement__tags=test__engagement__tags, test__engagement__product__tags__name=test__engagement__product__tags__name, not_tag=not_tag, not_tags=not_tags, not_test__tags=not_test__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__engagement__product__tags__name=not_test__engagement__product__tags__name, o=o, limit=limit, offset=offset, prefetch=prefetch, related_fields=related_fields)



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
    api_instance = openapi_client.FindingsApi(api_client)
    title = 'title_example' # str |  (optional)
date = 'date_example' # str |  (optional)
sla_start_date = 'sla_start_date_example' # str |  (optional)
cwe = 3.4 # float | Multiple values may be separated by commas. (optional)
cve = 'cve_example' # str |  (optional)
cvssv3 = 'cvssv3_example' # str |  (optional)
cvssv3_score = 3.4 # float |  (optional)
severity = 'severity_example' # str |  (optional)
description = 'description_example' # str |  (optional)
mitigation = 'mitigation_example' # str |  (optional)
impact = 'impact_example' # str |  (optional)
steps_to_reproduce = 'steps_to_reproduce_example' # str |  (optional)
severity_justification = 'severity_justification_example' # str |  (optional)
endpoints = 3.4 # float | Multiple values may be separated by commas. (optional)
references = 'references_example' # str |  (optional)
test = 'test_example' # str |  (optional)
active = 'active_example' # str |  (optional)
verified = 'verified_example' # str |  (optional)
false_p = 'false_p_example' # str |  (optional)
duplicate = 'duplicate_example' # str |  (optional)
duplicate_finding = 'duplicate_finding_example' # str |  (optional)
out_of_scope = 'out_of_scope_example' # str |  (optional)
risk_accepted = 'risk_accepted_example' # str |  (optional)
under_review = 'under_review_example' # str |  (optional)
last_status_update = 'last_status_update_example' # str |  (optional)
review_requested_by = 3.4 # float | Multiple values may be separated by commas. (optional)
reviewers = 3.4 # float | Multiple values may be separated by commas. (optional)
under_defect_review = 'under_defect_review_example' # str |  (optional)
defect_review_requested_by = 3.4 # float | Multiple values may be separated by commas. (optional)
is_mitigated = 'is_mitigated_example' # str |  (optional)
mitigated = 'mitigated_example' # str |  (optional)
mitigated_by = 3.4 # float | Multiple values may be separated by commas. (optional)
reporter = 3.4 # float | Multiple values may be separated by commas. (optional)
numerical_severity = 'numerical_severity_example' # str |  (optional)
last_reviewed = 'last_reviewed_example' # str |  (optional)
last_reviewed_by = 3.4 # float | Multiple values may be separated by commas. (optional)
param = 'param_example' # str |  (optional)
payload = 'payload_example' # str |  (optional)
hash_code = 'hash_code_example' # str |  (optional)
file_path = 'file_path_example' # str |  (optional)
component_name = 'component_name_example' # str |  (optional)
component_version = 'component_version_example' # str |  (optional)
found_by = 3.4 # float | Multiple values may be separated by commas. (optional)
static_finding = 'static_finding_example' # str |  (optional)
dynamic_finding = 'dynamic_finding_example' # str |  (optional)
created = 'created_example' # str |  (optional)
scanner_confidence = 3.4 # float | Multiple values may be separated by commas. (optional)
sonarqube_issue = 3.4 # float | Multiple values may be separated by commas. (optional)
unique_id_from_tool = 'unique_id_from_tool_example' # str |  (optional)
vuln_id_from_tool = 'vuln_id_from_tool_example' # str |  (optional)
sast_source_object = 'sast_source_object_example' # str |  (optional)
sast_sink_object = 'sast_sink_object_example' # str |  (optional)
sast_source_line = 3.4 # float | Multiple values may be separated by commas. (optional)
sast_source_file_path = 'sast_source_file_path_example' # str |  (optional)
nb_occurences = 3.4 # float | Multiple values may be separated by commas. (optional)
publish_date = 'publish_date_example' # str |  (optional)
service = 'service_example' # str |  (optional)
tags = 'tags_example' # str | Comma seperated list of exact tags (optional)
step_to_reproduce = 'step_to_reproduce_example' # str |  (optional)
jira_creation = 'jira_creation_example' # str |  (optional)
jira_change = 'jira_change_example' # str |  (optional)
id = 3.4 # float | Multiple values may be separated by commas. (optional)
test__test_type = 3.4 # float | Multiple values may be separated by commas. (optional)
test__engagement = 3.4 # float | Multiple values may be separated by commas. (optional)
test__engagement__product = 3.4 # float | Multiple values may be separated by commas. (optional)
finding_group = 3.4 # float | Multiple values may be separated by commas. (optional)
risk_acceptance = 'risk_acceptance_example' # str |  (optional)
tag = 'tag_example' # str | Tag name contains (optional)
test__tags = 'test__tags_example' # str | Comma seperated list of exact tags present on test (optional)
test__engagement__tags = 'test__engagement__tags_example' # str | Comma seperated list of exact tags present on engagement (optional)
test__engagement__product__tags__name = 'test__engagement__product__tags__name_example' # str | Comma seperated list of exact tags present on product (optional)
not_tag = 'not_tag_example' # str | Not Tag name contains (optional)
not_tags = 'not_tags_example' # str | Comma seperated list of exact tags not present on model (optional)
not_test__tags = 'not_test__tags_example' # str | Comma seperated list of exact tags not present on test (optional)
not_test__engagement__tags = 'not_test__engagement__tags_example' # str | Comma seperated list of exact tags not present on engagement (optional)
not_test__engagement__product__tags__name = 'not_test__engagement__product__tags__name_example' # str | Comma seperated list of exact tags not present on product (optional)
o = 'o_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
prefetch = ['prefetch_example'] # list[str] |  (optional)
related_fields = True # bool | Expand finding external relations (engagement, environment, product, product_type, test, test_type) (optional)

    try:
        api_response = api_instance.findings_list(title=title, date=date, sla_start_date=sla_start_date, cwe=cwe, cve=cve, cvssv3=cvssv3, cvssv3_score=cvssv3_score, severity=severity, description=description, mitigation=mitigation, impact=impact, steps_to_reproduce=steps_to_reproduce, severity_justification=severity_justification, endpoints=endpoints, references=references, test=test, active=active, verified=verified, false_p=false_p, duplicate=duplicate, duplicate_finding=duplicate_finding, out_of_scope=out_of_scope, risk_accepted=risk_accepted, under_review=under_review, last_status_update=last_status_update, review_requested_by=review_requested_by, reviewers=reviewers, under_defect_review=under_defect_review, defect_review_requested_by=defect_review_requested_by, is_mitigated=is_mitigated, mitigated=mitigated, mitigated_by=mitigated_by, reporter=reporter, numerical_severity=numerical_severity, last_reviewed=last_reviewed, last_reviewed_by=last_reviewed_by, param=param, payload=payload, hash_code=hash_code, file_path=file_path, component_name=component_name, component_version=component_version, found_by=found_by, static_finding=static_finding, dynamic_finding=dynamic_finding, created=created, scanner_confidence=scanner_confidence, sonarqube_issue=sonarqube_issue, unique_id_from_tool=unique_id_from_tool, vuln_id_from_tool=vuln_id_from_tool, sast_source_object=sast_source_object, sast_sink_object=sast_sink_object, sast_source_line=sast_source_line, sast_source_file_path=sast_source_file_path, nb_occurences=nb_occurences, publish_date=publish_date, service=service, tags=tags, step_to_reproduce=step_to_reproduce, jira_creation=jira_creation, jira_change=jira_change, id=id, test__test_type=test__test_type, test__engagement=test__engagement, test__engagement__product=test__engagement__product, finding_group=finding_group, risk_acceptance=risk_acceptance, tag=tag, test__tags=test__tags, test__engagement__tags=test__engagement__tags, test__engagement__product__tags__name=test__engagement__product__tags__name, not_tag=not_tag, not_tags=not_tags, not_test__tags=not_test__tags, not_test__engagement__tags=not_test__engagement__tags, not_test__engagement__product__tags__name=not_test__engagement__product__tags__name, o=o, limit=limit, offset=offset, prefetch=prefetch, related_fields=related_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | [optional] 
 **date** | **str**|  | [optional] 
 **sla_start_date** | **str**|  | [optional] 
 **cwe** | **float**| Multiple values may be separated by commas. | [optional] 
 **cve** | **str**|  | [optional] 
 **cvssv3** | **str**|  | [optional] 
 **cvssv3_score** | **float**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **mitigation** | **str**|  | [optional] 
 **impact** | **str**|  | [optional] 
 **steps_to_reproduce** | **str**|  | [optional] 
 **severity_justification** | **str**|  | [optional] 
 **endpoints** | **float**| Multiple values may be separated by commas. | [optional] 
 **references** | **str**|  | [optional] 
 **test** | **str**|  | [optional] 
 **active** | **str**|  | [optional] 
 **verified** | **str**|  | [optional] 
 **false_p** | **str**|  | [optional] 
 **duplicate** | **str**|  | [optional] 
 **duplicate_finding** | **str**|  | [optional] 
 **out_of_scope** | **str**|  | [optional] 
 **risk_accepted** | **str**|  | [optional] 
 **under_review** | **str**|  | [optional] 
 **last_status_update** | **str**|  | [optional] 
 **review_requested_by** | **float**| Multiple values may be separated by commas. | [optional] 
 **reviewers** | **float**| Multiple values may be separated by commas. | [optional] 
 **under_defect_review** | **str**|  | [optional] 
 **defect_review_requested_by** | **float**| Multiple values may be separated by commas. | [optional] 
 **is_mitigated** | **str**|  | [optional] 
 **mitigated** | **str**|  | [optional] 
 **mitigated_by** | **float**| Multiple values may be separated by commas. | [optional] 
 **reporter** | **float**| Multiple values may be separated by commas. | [optional] 
 **numerical_severity** | **str**|  | [optional] 
 **last_reviewed** | **str**|  | [optional] 
 **last_reviewed_by** | **float**| Multiple values may be separated by commas. | [optional] 
 **param** | **str**|  | [optional] 
 **payload** | **str**|  | [optional] 
 **hash_code** | **str**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **component_name** | **str**|  | [optional] 
 **component_version** | **str**|  | [optional] 
 **found_by** | **float**| Multiple values may be separated by commas. | [optional] 
 **static_finding** | **str**|  | [optional] 
 **dynamic_finding** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **scanner_confidence** | **float**| Multiple values may be separated by commas. | [optional] 
 **sonarqube_issue** | **float**| Multiple values may be separated by commas. | [optional] 
 **unique_id_from_tool** | **str**|  | [optional] 
 **vuln_id_from_tool** | **str**|  | [optional] 
 **sast_source_object** | **str**|  | [optional] 
 **sast_sink_object** | **str**|  | [optional] 
 **sast_source_line** | **float**| Multiple values may be separated by commas. | [optional] 
 **sast_source_file_path** | **str**|  | [optional] 
 **nb_occurences** | **float**| Multiple values may be separated by commas. | [optional] 
 **publish_date** | **str**|  | [optional] 
 **service** | **str**|  | [optional] 
 **tags** | **str**| Comma seperated list of exact tags | [optional] 
 **step_to_reproduce** | **str**|  | [optional] 
 **jira_creation** | **str**|  | [optional] 
 **jira_change** | **str**|  | [optional] 
 **id** | **float**| Multiple values may be separated by commas. | [optional] 
 **test__test_type** | **float**| Multiple values may be separated by commas. | [optional] 
 **test__engagement** | **float**| Multiple values may be separated by commas. | [optional] 
 **test__engagement__product** | **float**| Multiple values may be separated by commas. | [optional] 
 **finding_group** | **float**| Multiple values may be separated by commas. | [optional] 
 **risk_acceptance** | **str**|  | [optional] 
 **tag** | **str**| Tag name contains | [optional] 
 **test__tags** | **str**| Comma seperated list of exact tags present on test | [optional] 
 **test__engagement__tags** | **str**| Comma seperated list of exact tags present on engagement | [optional] 
 **test__engagement__product__tags__name** | **str**| Comma seperated list of exact tags present on product | [optional] 
 **not_tag** | **str**| Not Tag name contains | [optional] 
 **not_tags** | **str**| Comma seperated list of exact tags not present on model | [optional] 
 **not_test__tags** | **str**| Comma seperated list of exact tags not present on test | [optional] 
 **not_test__engagement__tags** | **str**| Comma seperated list of exact tags not present on engagement | [optional] 
 **not_test__engagement__product__tags__name** | **str**| Comma seperated list of exact tags not present on product | [optional] 
 **o** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 
 **related_fields** | **bool**| Expand finding external relations (engagement, environment, product, product_type, test, test_type) | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **findings_metadata_create**
> FindingMeta findings_metadata_create(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.FindingMeta() # FindingMeta | 

    try:
        api_response = api_instance.findings_metadata_create(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_metadata_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**FindingMeta**](FindingMeta.md)|  | 

### Return type

[**FindingMeta**](FindingMeta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |
**404** | Returned if finding does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_delete**
> findings_metadata_delete(id, name)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
name = 'name_example' # str | name of the metadata to retrieve. If name is empty, return all the                             metadata associated with the finding

    try:
        api_instance.findings_metadata_delete(id, name)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **name** | **str**| name of the metadata to retrieve. If name is empty, return all the                             metadata associated with the finding | 

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
**200** | Returned if the metadata was correctly deleted |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |
**404** | Returned if finding does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_read**
> list[FindingMeta] findings_metadata_read(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_metadata_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_metadata_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**list[FindingMeta]**](FindingMeta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Returned if finding does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_metadata_update**
> FindingMeta findings_metadata_update(id, name, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
name = 'name_example' # str | name of the metadata to edit
data = openapi_client.FindingMeta() # FindingMeta | 

    try:
        api_response = api_instance.findings_metadata_update(id, name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_metadata_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **name** | **str**| name of the metadata to edit | 
 **data** | [**FindingMeta**](FindingMeta.md)|  | 

### Return type

[**FindingMeta**](FindingMeta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Returned if there was a problem with the metadata information |  -  |
**404** | Returned if finding does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_create**
> Note findings_notes_create(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.AddNewNoteOption() # AddNewNoteOption | 

    try:
        api_response = api_instance.findings_notes_create(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
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

# **findings_notes_read**
> FindingToNotes findings_notes_read(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_notes_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**FindingToNotes**](FindingToNotes.md)

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

# **findings_partial_update**
> Finding findings_partial_update(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.Finding() # Finding | 

    try:
        api_response = api_instance.findings_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

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

# **findings_read**
> InlineResponse20011 findings_read(id, prefetch=prefetch, related_fields=related_fields)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
prefetch = ['prefetch_example'] # list[str] |  (optional)
related_fields = True # bool | Expand finding external relations (engagement, environment, product, product_type, test, test_type) (optional)

    try:
        api_response = api_instance.findings_read(id, prefetch=prefetch, related_fields=related_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **prefetch** | [**list[str]**](str.md)|  | [optional] 
 **related_fields** | **bool**| Expand finding external relations (engagement, environment, product, product_type, test, test_type) | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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

# **findings_remove_note**
> findings_remove_note(id, data)



Remove Note From Finding Note

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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.FindingNote() # FindingNote | 

    try:
        api_instance.findings_remove_note(id, data)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_remove_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**FindingNote**](FindingNote.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_partial_update**
> findings_remove_tags_partial_update(id, data)



Remove Tag(s) from finding list of tags

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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.Tag() # Tag | 

    try:
        api_instance.findings_remove_tags_partial_update(id, data)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_remove_tags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_update**
> findings_remove_tags_update(id, data)



Remove Tag(s) from finding list of tags

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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.Tag() # Tag | 

    try:
        api_instance.findings_remove_tags_update(id, data)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_remove_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_request_response_create**
> BurpRawRequestResponse findings_request_response_create(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.BurpRawRequestResponse() # BurpRawRequestResponse | 

    try:
        api_response = api_instance.findings_request_response_create(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_request_response_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**BurpRawRequestResponse**](BurpRawRequestResponse.md)|  | 

### Return type

[**BurpRawRequestResponse**](BurpRawRequestResponse.md)

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

# **findings_request_response_read**
> BurpRawRequestResponse findings_request_response_read(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_request_response_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_request_response_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**BurpRawRequestResponse**](BurpRawRequestResponse.md)

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

# **findings_set_finding_as_original**
> findings_set_finding_as_original(id, new_fid)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
new_fid = 'new_fid_example' # str | 

    try:
        api_instance.findings_set_finding_as_original(id, new_fid)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_set_finding_as_original: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **new_fid** | **str**|  | 

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

# **findings_tags_create**
> Tag findings_tags_create(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.Tag() # Tag | 

    try:
        api_response = api_instance.findings_tags_create(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

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

# **findings_tags_read**
> Tag findings_tags_read(id)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.

    try:
        api_response = api_instance.findings_tags_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**Tag**](Tag.md)

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

# **findings_update**
> Finding findings_update(id, data)



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
    api_instance = openapi_client.FindingsApi(api_client)
    id = 56 # int | A unique integer value identifying this finding.
data = openapi_client.Finding() # Finding | 

    try:
        api_response = api_instance.findings_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FindingsApi->findings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

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

