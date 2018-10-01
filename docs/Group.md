# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name of group | [optional] 
**user_count** | **int** | Number of users included in this group | [optional] 
**contains_current_user** | **bool** | Currently logged in user is group member | [optional] 
**externally_managed** | **bool** | Group membership controlled outside of Looker | [optional] 
**include_by_default** | **bool** | New users are added to this group by default | [optional] 
**external_group_id** | **str** | External Id group if embed group | [optional] 
**can_add_to_content_metadata** | **bool** | Group can be used in content access controls | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


