# LookmlModelExploreJoins

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of this join (and name of the view to join) | [optional] 
**dependent_fields** | **list[str]** | Fields referenced by the join | [optional] 
**fields** | **list[str]** | Fields of the joined view to pull into this explore | [optional] 
**foreign_key** | **str** | Name of the dimension in this explore whose value is in the primary key of the joined view | [optional] 
**_from** | **str** | Name of view to join | [optional] 
**outer_only** | **bool** | Specifies whether all queries must use an outer join | [optional] 
**relationship** | **str** | many_to_one, one_to_one, one_to_many, many_to_many | [optional] 
**required_joins** | **list[str]** | Names of joins that must always be included in SQL queries | [optional] 
**sql_foreign_key** | **str** | SQL expression that produces a foreign key | [optional] 
**sql_on** | **str** | SQL ON expression describing the join condition | [optional] 
**sql_table_name** | **str** | SQL table name to join | [optional] 
**type** | **str** | The join type: left_outer, full_outer, inner, or cross | [optional] 
**view_label** | **str** | Label to display in UI selectors | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


