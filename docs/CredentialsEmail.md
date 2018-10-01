# CredentialsEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | EMail address used for user login | [optional] 
**created_at** | **str** | Timestamp for the creation of this credential | [optional] 
**logged_in_at** | **str** | Timestamp for most recent login using credential | [optional] 
**is_disabled** | **bool** | Has this credential been disabled? | [optional] 
**type** | **str** | Short name for the type of this kind of credential | [optional] 
**password_reset_url** | **str** | Url with one-time use secret token that the user can use to reset password | [optional] 
**forced_password_reset_at_next_login** | **bool** | Force the user to change their password upon their next login | [optional] 
**url** | **str** | Link to get this item | [optional] 
**user_url** | **str** | Link to get this user | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


