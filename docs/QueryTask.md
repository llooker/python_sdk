# QueryTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id | [optional] 
**query_id** | **int** | Id of query | [optional] 
**query** | [**Query**](Query.md) | Query | [optional] 
**generate_links** | **bool** | whether or not to generate links in the query response. | [optional] 
**force_production** | **bool** | Use production models to run query (even is user is in dev mode). | [optional] 
**path_prefix** | **str** | Prefix to use for drill links. | [optional] 
**cache** | **bool** | Whether or not to use the cache | [optional] 
**server_table_calcs** | **bool** | Whether or not to run table calculations on the server | [optional] 
**cache_only** | **bool** | Retrieve any results from cache even if the results have expired. | [optional] 
**cache_key** | **str** | cache key used to cache query. | [optional] 
**status** | **str** | Status of query task. | [optional] 
**source** | **str** | Source of query task. | [optional] 
**runtime** | **float** | Runtime of prior queries. | [optional] 
**rebuild_pdts** | **bool** | Rebuild PDTS used in query. | [optional] 
**result_source** | **str** | Source of the results of the query. | [optional] 
**look_id** | **int** | Id of look associated with query. | [optional] 
**dashboard_id** | **str** | Id of dashboard associated with query. | [optional] 
**result_format** | **str** | The data format of the query results. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


