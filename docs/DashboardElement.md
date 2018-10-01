# DashboardElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id | [optional] 
**dashboard_id** | **str** | Id of Dashboard | [optional] 
**look_id** | **str** | Id Of Look | [optional] 
**query_id** | **int** | Id Of Query | [optional] 
**type** | **str** | Type | [optional] 
**refresh_interval** | **str** | Refresh Interval | [optional] 
**refresh_interval_to_i** | **int** | Refresh Interval as integer | [optional] 
**note_text** | **str** | Note Text | [optional] 
**note_text_as_html** | **str** | Note Text as Html | [optional] 
**note_display** | **str** | Note Display | [optional] 
**note_state** | **str** | Note State | [optional] 
**title_hidden** | **bool** | Whether title is hidden | [optional] 
**title_text** | **str** | Text tile title | [optional] 
**title** | **str** | Title of dashboard element | [optional] 
**subtitle_text** | **str** | Text tile subtitle text | [optional] 
**body_text** | **str** | Text tile body text | [optional] 
**body_text_as_html** | **str** | Text tile body text as Html | [optional] 
**look** | [**LookWithQuery**](LookWithQuery.md) | Look | [optional] 
**query** | [**Query**](Query.md) | Query | [optional] 
**edit_uri** | **str** | Relative path of URI of LookML file to edit the dashboard element (LookML dashboard only). | [optional] 
**merge_result_id** | **str** | ID of merge result | [optional] 
**result_maker_id** | **int** | ID of the ResultMakerLookup entry. | [optional] 
**result_maker** | [**ResultMakerWithIdVisConfigAndDynamicFields**](ResultMakerWithIdVisConfigAndDynamicFields.md) | Data about the result maker. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


