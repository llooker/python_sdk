# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Project Id | [optional] 
**name** | **str** | Project display name | [optional] 
**uses_git** | **bool** | If true the project is configured with a git repository | [optional] 
**git_remote_url** | **str** | Git remote repository url | [optional] 
**git_username** | **str** | Git username for HTTPS authentication. (For production only, if using user attributes.) | [optional] 
**git_password** | **str** | (Write-Only) Git password for HTTPS authentication. (For production only, if using user attributes.) | [optional] 
**git_username_user_attribute** | **str** | User attribute name for username in per-user HTTPS authentication. | [optional] 
**git_password_user_attribute** | **str** | User attribute name for password in per-user HTTPS authentication. | [optional] 
**git_service_name** | **str** | Name of the git service provider | [optional] 
**pull_request_mode** | **str** | The git pull request policy for this project. Valid values are: \&quot;off\&quot;, \&quot;links\&quot;, \&quot;recommended\&quot;, \&quot;required\&quot;. | [optional] 
**validation_required** | **bool** | Validation policy: If true, the project must pass all validation checks before project changes can be committed to the git repository | [optional] 
**is_example** | **bool** | If true the project is an example project and cannot be modified | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


