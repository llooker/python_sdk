# DataActionFormField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**label** | **str** | Human-readable label | [optional] 
**description** | **str** | Description of field | [optional] 
**type** | **str** | Type of field. | [optional] 
**default** | **str** | Default value of the field. | [optional] 
**required** | **bool** | Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation. | [optional] 
**options** | [**list[DataActionFormSelectOption]**](DataActionFormSelectOption.md) | If the form type is &#39;select&#39;, a list of options to be selected from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


