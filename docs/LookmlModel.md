# LookmlModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model. Also used as the unique identifier | [optional] 
**project_name** | **str** | Name of project containing the model | [optional] 
**allowed_db_connection_names** | **list[str]** | Array of names of connections this model is allowed to use | [optional] 
**unlimited_db_connections** | **bool** | Is this model allowed to use all current and future connections | [optional] 
**has_content** | **bool** | Does this model declaration have have lookml content? | [optional] 
**label** | **str** | UI-friendly name for this model | [optional] 
**explores** | [**list[LookmlModelNavExplore]**](LookmlModelNavExplore.md) | Array of explores (if has_content) | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


