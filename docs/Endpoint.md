# Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**tags** | **list[str]** |  | [optional] 
**protocol** | **str** | The communication protocol/scheme such as &#39;http&#39;, &#39;ftp&#39;, &#39;dns&#39;, etc. | [optional] 
**userinfo** | **str** | User info as &#39;alice&#39;, &#39;bob&#39;, etc. | [optional] 
**host** | **str** | The host name or IP address. It must not include the port number. For example &#39;127.0.0.1&#39;, &#39;localhost&#39;, &#39;yourdomain.com&#39;. | [optional] 
**port** | **int** | The network port associated with the endpoint. | [optional] 
**path** | **str** | The location of the resource, it must not start with a &#39;/&#39;. For example endpoint/420/edit | [optional] 
**query** | **str** | The query string, the question mark should be omitted.For example &#39;group&#x3D;4&amp;team&#x3D;8&#39; | [optional] 
**fragment** | **str** | The fragment identifier which follows the hash mark. The hash mark should be omitted. For example &#39;section-13&#39;, &#39;paragraph-2&#39;. | [optional] 
**product** | **int** |  | [optional] 
**endpoint_params** | **list[int]** |  | [optional] [readonly] 
**endpoint_status** | **list[int]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


