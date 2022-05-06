# InlineResponse20048

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**test_import_finding_action_set** | [**list[TestImportFindingAction]**](TestImportFindingAction.md) |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**import_settings** | [**object**](.md) |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**build_id** | **str** | Build ID that was tested, a reimport may update this field. | [optional] 
**commit_hash** | **str** | Commit hash tested, a reimport may update this field. | [optional] 
**branch_tag** | **str** | Tag or branch that was tested, a reimport may update this field. | [optional] 
**test** | **int** |  | [optional] [readonly] 
**findings_affected** | **list[int]** |  | [optional] [readonly] 
**prefetch** | [**InlineResponse20047Prefetch**](InlineResponse20047Prefetch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


