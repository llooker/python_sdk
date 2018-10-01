# DashboardFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id | [optional] 
**dashboard_id** | **str** | Id of Dashboard | [optional] 
**name** | **str** | Name of filter | 
**title** | **str** | Title of filter | 
**type** | **str** | Type of filter: one of date, number, string, or field | 
**default_value** | **str** | Default value of filter | [optional] 
**model** | **str** | Model of filter (required if type &#x3D; field) | [optional] 
**explore** | **str** | Explore of filter (required if type &#x3D; field) | [optional] 
**dimension** | **str** | Dimension of filter (required if type &#x3D; field) | [optional] 
**field** | **dict(str, str)** | Field information | [optional] 
**row** | **int** | Display order of this filter relative to other filters | [optional] 
**listens_to_filters** | **list[str]** | Array of listeners for faceted filters | [optional] 
**allow_multiple_values** | **bool** | Whether the filter allows multiple filter values | [optional] 
**required** | **bool** | Whether the filter requires a value to run the dashboard | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


