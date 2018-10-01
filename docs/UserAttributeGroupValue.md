# UserAttributeGroupValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id of this group-attribute relation | [optional] 
**group_id** | **int** | Id of group | [optional] 
**user_attribute_id** | **int** | Id of user attribute | [optional] 
**value_is_hidden** | **bool** | If true, the \&quot;value\&quot; field will be null, because the attribute settings block access to this value | [optional] 
**rank** | **int** | Precedence for resolving value for user | [optional] 
**value** | **str** | Value of user attribute for group | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


