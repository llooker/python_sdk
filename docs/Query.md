# Query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**model** | **str** | Model | 
**view** | **str** | View | 
**fields** | **list[str]** | Fields | [optional] 
**pivots** | **list[str]** | Pivots | [optional] 
**fill_fields** | **list[str]** | Fill Fields | [optional] 
**filters** | **dict(str, str)** | Filters | [optional] 
**filter_expression** | **str** | Filter Expression | [optional] 
**sorts** | **list[str]** | Sorting for the query results. Use the format [\&quot;view.field\&quot;, ...] to sort on fields in ascending order. Use the format [\&quot;view.field desc\&quot;, ...] to sort on fields in descending order. Use [\&quot;__UNSORTED__\&quot;] to disable sorting entirely. Empty sorts [] will trigger a default sort. | [optional] 
**limit** | **str** | Limit | [optional] 
**column_limit** | **str** | Column Limit | [optional] 
**total** | **bool** | Total | [optional] 
**row_total** | **str** | Raw Total | [optional] 
**runtime** | **float** | Runtime | [optional] 
**vis_config** | **dict(str, str)** | Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A \&quot;type\&quot; key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties. | [optional] 
**filter_config** | **dict(str, str)** | The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over \&quot;filters\&quot;. When creating a query or modifying an existing query, \&quot;filter_config\&quot; should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque. | [optional] 
**visible_ui_sections** | **str** | Visible UI Sections | [optional] 
**slug** | **str** | Slug | [optional] 
**dynamic_fields** | **list[str]** | Dynamic Fields | [optional] 
**client_id** | **str** | Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated. | [optional] 
**share_url** | **str** | Share Url | [optional] 
**expanded_share_url** | **str** | Expanded Share Url | [optional] 
**url** | **str** | Expanded Url | [optional] 
**query_timezone** | **str** | Query Timezone | [optional] 
**has_table_calculations** | **bool** | Has Table Calculations | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


