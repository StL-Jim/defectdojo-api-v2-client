# Engagement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**tags** | **list[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** | Version of the product the engagement tested. | [optional] 
**first_contacted** | **date** |  | [optional] 
**target_start** | **date** |  | 
**target_end** | **date** |  | 
**reason** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**tracker** | **str** | Link to epic or ticket system with changes to version. | [optional] 
**test_strategy** | **str** |  | [optional] 
**threat_model** | **bool** |  | [optional] 
**api_test** | **bool** |  | [optional] 
**pen_test** | **bool** |  | [optional] 
**check_list** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**progress** | **str** |  | [optional] [readonly] 
**tmodel_path** | **str** |  | [optional] [readonly] 
**done_testing** | **bool** |  | [optional] [readonly] 
**engagement_type** | **str** |  | [optional] 
**build_id** | **str** | Build ID of the product the engagement tested. | [optional] 
**commit_hash** | **str** | Commit hash from repo | [optional] 
**branch_tag** | **str** | Tag or branch of the product the engagement tested. | [optional] 
**source_code_management_uri** | **str** | Resource link to source code | [optional] 
**deduplication_on_engagement** | **bool** | If enabled deduplication will only mark a finding in this engagement as duplicate of another finding if both findings are in this engagement. If disabled, deduplication is on the product level. | [optional] 
**lead** | **int** |  | [optional] 
**requester** | **int** |  | [optional] 
**preset** | **int** | Settings and notes for performing this engagement. | [optional] 
**report_type** | **int** |  | [optional] 
**product** | **int** |  | 
**build_server** | **int** | Build server responsible for CI/CD test | [optional] 
**source_code_management_server** | **int** | Source code server for CI/CD test | [optional] 
**orchestration_engine** | **int** | Orchestration service responsible for CI/CD test | [optional] 
**notes** | [**list[Note]**](Note.md) |  | [optional] [readonly] 
**files** | [**list[File]**](File.md) |  | [optional] [readonly] 
**risk_acceptance** | **list[int]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


