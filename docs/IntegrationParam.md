# IntegrationParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the parameter. | [optional] 
**label** | **str** | Label of the parameter. | [optional] 
**description** | **str** | Short description of the parameter. | [optional] 
**required** | **bool** | Whether the parameter is required to be set to use the destination. | [optional] 
**has_value** | **bool** | Whether the parameter has a value set. | [optional] 
**value** | **str** | The current value of the parameter. Always null if the value is sensitive. When writing, null values will be ignored. Set the value to an empty string to clear it. | [optional] 
**user_attribute_name** | **str** | When present, the param&#39;s value comes from this user attribute instead of the &#39;value&#39; parameter. Set to null to use the &#39;value&#39;. | [optional] 
**sensitive** | **bool** | Whether the parameter contains sensitive data like API credentials. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


