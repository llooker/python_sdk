# Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name of Role | [optional] 
**permission_set** | [**PermissionSet**](PermissionSet.md) | (Read only) Permission set | [optional] 
**permission_set_id** | **int** | (Write-Only) Id of permission set | [optional] 
**model_set** | [**ModelSet**](ModelSet.md) | (Read only) Model set | [optional] 
**model_set_id** | **int** | (Write-Only) Id of model set | [optional] 
**url** | **str** | Link to get this item | [optional] 
**users_url** | **str** | Link to get list of users with this role | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


