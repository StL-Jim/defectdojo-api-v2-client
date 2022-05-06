# RiskAcceptance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Descriptive name which in the future may also be used to group risk acceptances together across engagements and products | 
**recommendation** | **str** | Recommendation from the security team. | [optional] 
**recommendation_details** | **str** | Explanation of security recommendation | [optional] 
**decision** | **str** | Risk treatment decision by risk owner | [optional] 
**decision_details** | **str** | If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s). | [optional] 
**accepted_by** | **str** | The person that accepts the risk, can be outside of DefectDojo. | [optional] 
**path** | **str** |  | [optional] [readonly] 
**expiration_date** | **datetime** | When the risk acceptance expires, the findings will be reactivated (unless disabled below). | [optional] 
**expiration_date_warned** | **datetime** | (readonly) Date at which notice about the risk acceptance expiration was sent. | [optional] 
**expiration_date_handled** | **datetime** | (readonly) When the risk acceptance expiration was handled (manually or by the daily job). | [optional] 
**reactivate_expired** | **bool** | Reactivate findings when risk acceptance expires? | [optional] 
**restart_sla_expired** | **bool** | When enabled, the SLA for findings is restarted when the risk acceptance expires. | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**updated** | **datetime** |  | [optional] [readonly] 
**owner** | **int** | User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance. | 
**accepted_findings** | **list[int]** |  | 
**notes** | **list[int]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


