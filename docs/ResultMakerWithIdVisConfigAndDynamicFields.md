# ResultMakerWithIdVisConfigAndDynamicFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id. | [optional] 
**dynamic_fields** | **str** | JSON string of dynamic field information. | [optional] 
**filterables** | [**list[ResultMakerFilterables]**](ResultMakerFilterables.md) | array of items that can be filtered and information about them. | [optional] 
**sorts** | **str** | Sorts of the constituent Look, Query, or Merge Query | [optional] 
**merge_result_id** | **str** | ID of merge result if this is a merge_result. | [optional] 
**total** | **bool** | Total of the constituent Look, Query, or Merge Query | [optional] 
**query_id** | **int** | ID of query if this is a query. | [optional] 
**query** | [**Query**](Query.md) | Query | [optional] 
**vis_config** | **str** | Vis config of the constituent Query, or Merge Query. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


