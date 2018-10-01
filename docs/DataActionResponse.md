# DataActionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | ID of the webhook event that sent this data action. In some error conditions, this may be null. | [optional] 
**success** | **bool** | Whether the data action was successful. | [optional] 
**refresh_query** | **bool** | When true, indicates that the client should refresh (rerun) the source query because the data may have been changed by the action. | [optional] 
**validation_errors** | [**ValidationError**](ValidationError.md) | Validation errors returned by the data action server. | [optional] 
**message** | **str** | Optional message returned by the data action server describing the state of the action that took place. This can be used to implement custom failure messages. If a failure is related to a particular form field, the server should send back a validation error instead. The Looker web UI does not currently display any message if the action indicates &#39;success&#39;, but may do so in the future. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


