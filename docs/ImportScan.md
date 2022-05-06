# ImportScan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_date** | **date** |  | [optional] 
**minimum_severity** | **str** |  | [optional] [default to 'Info']
**active** | **bool** |  | [optional] [default to True]
**verified** | **bool** |  | [optional] [default to True]
**scan_type** | **str** |  | 
**endpoint_to_add** | **int** |  | [optional] 
**file** | **str** |  | [optional] [readonly] 
**product_type_name** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**engagement_name** | **str** |  | [optional] 
**engagement** | **int** |  | [optional] 
**test_title** | **str** |  | [optional] 
**auto_create_context** | **bool** |  | [optional] 
**lead** | **int** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**close_old_findings** | **bool** | Select if old findings no longer present in the report get closed as mitigated when importing. If service has been set, only the findings for this service will be closed. | [optional] [default to False]
**push_to_jira** | **bool** |  | [optional] [default to False]
**environment** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** |  | [optional] 
**branch_tag** | **str** |  | [optional] 
**commit_hash** | **str** |  | [optional] 
**api_scan_configuration** | **int** |  | [optional] 
**service** | **str** | A service is a self-contained piece of functionality within a Product. This is an optional field which is used in deduplication and closing of old findings when set. This affects the whole engagement/product depending on your deduplication scope. | [optional] 
**group_by** | **str** | Choose an option to automatically group new findings by the chosen option. | [optional] 
**test** | **int** |  | [optional] [readonly] 
**test_id** | **int** |  | [optional] [readonly] 
**engagement_id** | **int** |  | [optional] [readonly] 
**product_id** | **int** |  | [optional] [readonly] 
**product_type_id** | **int** |  | [optional] [readonly] 
**statistics** | [**ImportStatistics**](ImportStatistics.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


