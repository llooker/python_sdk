# RenderTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of this render task | [optional] 
**created_at** | **str** | Date/Time render task was created | [optional] 
**finalized_at** | **str** | Date/Time render task was completed | [optional] 
**status** | **str** | Render task status: enqueued_for_query, querying, enqueued_for_render, rendering, success, failure | [optional] 
**status_detail** | **str** | Additional information about the current status | [optional] 
**user_id** | **int** | The user account permissions in which the render task will execute | [optional] 
**runtime** | **float** | Total seconds elapsed for render task | [optional] 
**query_runtime** | **float** | Number of seconds elapsed running queries | [optional] 
**render_runtime** | **float** | Number of seconds elapsed rendering data | [optional] 
**result_format** | **str** | Output format: pdf, png, or jpg | [optional] 
**look_id** | **int** | Id of look to render | [optional] 
**dashboard_id** | **int** | Id of dashboard to render | [optional] 
**lookml_dashboard_id** | **str** | Id of lookml dashboard to render | [optional] 
**query_id** | **int** | Id of query to render | [optional] 
**width** | **int** | Output width in pixels | [optional] 
**height** | **int** | Output height in pixels. Flowed layouts may ignore this value. | [optional] 
**dashboard_style** | **str** | Dashboard layout style: single_column or tiled | [optional] 
**dashboard_filters** | **str** | Filter values to apply to the dashboard queries, in URL query format | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


