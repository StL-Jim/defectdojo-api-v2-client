# JIRAProject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**project_key** | **str** |  | [optional] 
**issue_template_dir** | **str** | Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates. | [optional] 
**component** | **str** |  | [optional] 
**push_all_issues** | **bool** | Automatically maintain parity with JIRA. Always create and update JIRA tickets for findings in this Product. | [optional] 
**enable_engagement_epic_mapping** | **bool** |  | [optional] 
**push_notes** | **bool** |  | [optional] 
**product_jira_sla_notification** | **bool** |  | [optional] 
**risk_acceptance_expiration_notification** | **bool** |  | [optional] 
**jira_instance** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**engagement** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


