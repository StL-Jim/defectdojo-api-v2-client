# Test

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**tags** | **list[str]** |  | [optional] 
**test_type_name** | **str** |  | [optional] [readonly] 
**finding_groups** | [**list[FindingGroup]**](FindingGroup.md) |  | [optional] [readonly] 
**scan_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**target_start** | **datetime** |  | 
**target_end** | **datetime** |  | 
**estimated_time** | **str** |  | [optional] [readonly] 
**actual_time** | **str** |  | [optional] [readonly] 
**percent_complete** | **int** |  | [optional] 
**updated** | **datetime** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**engagement** | **int** |  | [optional] [readonly] 
**lead** | **int** |  | [optional] 
**test_type** | **int** |  | 
**environment** | **int** |  | [optional] 
**api_scan_configuration** | **int** |  | [optional] 
**notes** | [**list[Note]**](Note.md) |  | [optional] [readonly] 
**files** | [**list[File]**](File.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


