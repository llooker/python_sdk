# CredentialsEmbed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**external_user_id** | **str** | Embedder&#39;s unique id for the user | [optional] 
**external_group_id** | **str** | Embedder&#39;s id for a group to which this user was added during the most recent login | [optional] 
**created_at** | **str** | Timestamp for the creation of this credential | [optional] 
**logged_in_at** | **str** | Timestamp for most recent login using credential | [optional] 
**is_disabled** | **bool** | Has this credential been disabled? | [optional] 
**type** | **str** | Short name for the type of this kind of credential | [optional] 
**url** | **str** | Link to get this item | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


