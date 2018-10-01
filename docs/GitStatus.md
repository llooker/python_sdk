# GitStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Git action: add, delete, etc | [optional] 
**text** | **str** | Git description of the action | [optional] 
**revertable** | **bool** | When true, the file can be reverted to an earlier state | [optional] 
**conflict** | **bool** | When true, changes to the local file conflict with the remote repository | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


