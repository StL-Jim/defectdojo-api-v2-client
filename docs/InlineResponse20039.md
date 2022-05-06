# InlineResponse20039

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**findings_count** | **int** |  | [optional] [readonly] 
**findings_list** | **list[int]** |  | [optional] [readonly] 
**tags** | **list[str]** |  | [optional] 
**product_meta** | [**list[ProductMeta]**](ProductMeta.md) |  | [optional] [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 
**created** | **datetime** |  | [optional] [readonly] 
**prod_numeric_grade** | **int** |  | [optional] 
**business_criticality** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**lifecycle** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**user_records** | **int** | Estimate the number of user records within the application. | [optional] 
**revenue** | **str** | Estimate the application&#39;s revenue. | [optional] 
**external_audience** | **bool** | Specify if the application is used by people outside the organization. | [optional] 
**internet_accessible** | **bool** | Specify if the application is accessible from the public internet. | [optional] 
**enable_simple_risk_acceptance** | **bool** | Allows simple risk acceptance by checking/unchecking a checkbox. | [optional] 
**enable_full_risk_acceptance** | **bool** | Allows full risk acceptance using a risk acceptance form, expiration date, uploaded proof, etc. | [optional] 
**product_manager** | **int** |  | [optional] 
**technical_contact** | **int** |  | [optional] 
**team_manager** | **int** |  | [optional] 
**prod_type** | **int** |  | 
**members** | **list[int]** |  | [optional] [readonly] 
**authorization_groups** | **list[int]** |  | [optional] [readonly] 
**regulations** | **list[int]** |  | [optional] 
**prefetch** | [**InlineResponse20038Prefetch**](InlineResponse20038Prefetch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


