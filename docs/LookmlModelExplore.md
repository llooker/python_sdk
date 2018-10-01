# LookmlModelExplore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fully qualified name model plus explore name | [optional] 
**name** | **str** | Explore name | [optional] 
**description** | **str** | Description | [optional] 
**label** | **str** | Label | [optional] 
**scopes** | **list[str]** | Scopes | [optional] 
**can_total** | **bool** | Can Total | [optional] 
**can_save** | **bool** | Can Save | [optional] 
**can_explain** | **bool** | Can Explain | [optional] 
**can_pivot_in_db** | **bool** | Can pivot in the DB | [optional] 
**has_timezone_support** | **bool** | Has timezone support | [optional] 
**supports_cost_estimate** | **bool** | Cost estimates supported | [optional] 
**connection_name** | **str** | Connection name | [optional] 
**null_sort_treatment** | **str** | How nulls are sorted, possible values are \&quot;low\&quot;, \&quot;high\&quot;, \&quot;first\&quot; and \&quot;last\&quot; | [optional] 
**files** | **list[str]** | List of model source files | [optional] 
**source_file** | **str** | Primary source_file file | [optional] 
**project_name** | **str** | Name of project | [optional] 
**model_name** | **str** | Name of model | [optional] 
**view_name** | **str** | Name of view | [optional] 
**hidden** | **bool** | Is hidden | [optional] 
**sql_table_name** | **str** | A sql_table_name expression that defines what sql table the view/explore maps onto. Example: \&quot;prod_orders2 AS orders\&quot; in a view named orders. | [optional] 
**access_filter_fields** | **list[str]** | (DEPRECATED) Array of access filter field names | [optional] 
**access_filters** | [**list[LookmlModelExploreAccessFilter]**](LookmlModelExploreAccessFilter.md) | Access filters | [optional] 
**aliases** | [**list[LookmlModelExploreAlias]**](LookmlModelExploreAlias.md) | Aliases | [optional] 
**always_filter** | [**list[LookmlModelExploreAlwaysFilter]**](LookmlModelExploreAlwaysFilter.md) | Always filter | [optional] 
**conditionally_filter** | [**list[LookmlModelExploreConditionallyFilter]**](LookmlModelExploreConditionallyFilter.md) | Conditionally filter | [optional] 
**index_fields** | **list[str]** | Array of index fields | [optional] 
**sets** | [**list[LookmlModelExploreSet]**](LookmlModelExploreSet.md) | Sets | [optional] 
**errors** | [**list[LookmlModelExploreError]**](LookmlModelExploreError.md) | Errors | [optional] 
**fields** | [**LookmlModelExploreFieldset**](LookmlModelExploreFieldset.md) | Fields | [optional] 
**joins** | [**list[LookmlModelExploreJoins]**](LookmlModelExploreJoins.md) | Views joined into this explore | [optional] 
**group_label** | **str** | Label used to group explores in the navigation menus | [optional] 
**supported_measure_types** | [**list[LookmlModelExploreSupportedMeasureType]**](LookmlModelExploreSupportedMeasureType.md) | An array of items describing which custom measure types are supported for creating a custom measure &#39;baed_on&#39; each possible dimension type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


