# openapi_client.ReimportScanApi

All URIs are relative to *https://demo.defectdojo.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reimport_scan_create**](ReimportScanApi.md#reimport_scan_create) | **POST** /reimport-scan/ | Reimports a scan report into an existing test.


# **reimport_scan_create**
> ReImportScan reimport_scan_create(scan_type, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, product_type_name=product_type_name, product_name=product_name, engagement_name=engagement_name, test=test, test_title=test_title, auto_create_context=auto_create_context, push_to_jira=push_to_jira, close_old_findings=close_old_findings, version=version, build_id=build_id, branch_tag=branch_tag, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, service=service, environment=environment, lead=lead, tags=tags, group_by=group_by)

Reimports a scan report into an existing test.

By ID: - Create a Product (or use an existing product) - Create an Engagement inside the product - Import a scan report and find the id of the Test - Provide this in the `test` parameter  By Names: - Create a Product (or use an existing product) - Create an Engagement inside the product - Import a report which will create a Test - Provide `product_name` - Provide `engagement_name` - Optional: Provide `test_title`  In this scenario Defect Dojo will look up the Test by the provided details. If no `test_title` is provided, the latest test inside the engagement will be chosen based on scan_type.  When using names you can let the importer automatically create Engagements, Products and Product_Types by using `auto_create_context=True`.

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
    api_instance = openapi_client.ReimportScanApi(api_client)
    scan_type = 'scan_type_example' # str | 
scan_date = '2013-10-20' # date |  (optional)
minimum_severity = 'Info' # str |  (optional) (default to 'Info')
active = True # bool |  (optional) (default to True)
verified = True # bool |  (optional) (default to True)
endpoint_to_add = 56 # int |  (optional)
file = '/path/to/file' # file |  (optional)
product_type_name = 'product_type_name_example' # str |  (optional)
product_name = 'product_name_example' # str |  (optional)
engagement_name = 'engagement_name_example' # str |  (optional)
test = 56 # int |  (optional)
test_title = 'test_title_example' # str |  (optional)
auto_create_context = True # bool |  (optional)
push_to_jira = False # bool |  (optional) (default to False)
close_old_findings = True # bool |  (optional) (default to True)
version = 'version_example' # str |  (optional)
build_id = 'build_id_example' # str |  (optional)
branch_tag = 'branch_tag_example' # str |  (optional)
commit_hash = 'commit_hash_example' # str |  (optional)
api_scan_configuration = 56 # int |  (optional)
service = 'service_example' # str | A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope. (optional)
environment = 'environment_example' # str |  (optional)
lead = 56 # int |  (optional)
tags = 'tags_example' # list[str] |  (optional)
group_by = 'group_by_example' # str | Choose an option to automatically group new findings by the chosen option. (optional)

    try:
        # Reimports a scan report into an existing test.
        api_response = api_instance.reimport_scan_create(scan_type, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, product_type_name=product_type_name, product_name=product_name, engagement_name=engagement_name, test=test, test_title=test_title, auto_create_context=auto_create_context, push_to_jira=push_to_jira, close_old_findings=close_old_findings, version=version, build_id=build_id, branch_tag=branch_tag, commit_hash=commit_hash, api_scan_configuration=api_scan_configuration, service=service, environment=environment, lead=lead, tags=tags, group_by=group_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReimportScanApi->reimport_scan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_type** | **str**|  | 
 **scan_date** | **date**|  | [optional] 
 **minimum_severity** | **str**|  | [optional] [default to &#39;Info&#39;]
 **active** | **bool**|  | [optional] [default to True]
 **verified** | **bool**|  | [optional] [default to True]
 **endpoint_to_add** | **int**|  | [optional] 
 **file** | **file**|  | [optional] 
 **product_type_name** | **str**|  | [optional] 
 **product_name** | **str**|  | [optional] 
 **engagement_name** | **str**|  | [optional] 
 **test** | **int**|  | [optional] 
 **test_title** | **str**|  | [optional] 
 **auto_create_context** | **bool**|  | [optional] 
 **push_to_jira** | **bool**|  | [optional] [default to False]
 **close_old_findings** | **bool**|  | [optional] [default to True]
 **version** | **str**|  | [optional] 
 **build_id** | **str**|  | [optional] 
 **branch_tag** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **api_scan_configuration** | **int**|  | [optional] 
 **service** | **str**| A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope. | [optional] 
 **environment** | **str**|  | [optional] 
 **lead** | **int**|  | [optional] 
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **group_by** | **str**| Choose an option to automatically group new findings by the chosen option. | [optional] 

### Return type

[**ReImportScan**](ReImportScan.md)

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

