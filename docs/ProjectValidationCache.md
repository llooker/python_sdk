# ProjectValidationCache

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[ProjectError]**](ProjectError.md) | A list of project errors | [optional] 
**project_digest** | **str** | A hash value computed from the project&#39;s current state | [optional] 
**models_not_validated** | [**list[ModelsNotValidated]**](ModelsNotValidated.md) | A list of models which were not fully validated | [optional] 
**stale** | **bool** | If true, the cached project validation results are no longer accurate because the project has changed since the cached results were calculated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


