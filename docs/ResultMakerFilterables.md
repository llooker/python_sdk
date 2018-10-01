# ResultMakerFilterables

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model this filterable comes from (used for field suggestions). | [optional] 
**view** | **str** | The view this filterable comes from (used for field suggestions). | [optional] 
**name** | **str** | The name of the filterable thing (Query or Merged Results). | [optional] 
**listen** | [**list[ResultMakerFilterablesListen]**](ResultMakerFilterablesListen.md) | array of dashboard_filter_name: and field: objects. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


