# ProjectFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An opaque token uniquely identifying a file within a project. Avoid parsing or decomposing the text of this token. This token is stable within a Looker release but may change between Looker releases | [optional] 
**path** | **str** | Path, file name, and extension of the file relative to the project root directory | [optional] 
**title** | **str** | Display name | [optional] 
**type** | **str** | File type: model, view, etc | [optional] 
**mime_type** | **str** | File mime type | [optional] 
**git_status** | [**GitStatus**](GitStatus.md) | Status of the file according to git | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


