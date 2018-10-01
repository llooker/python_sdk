# Look

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**content_metadata_id** | **int** | Id of content metadata | [optional] 
**view_count** | **int** | Number of times viewed in the Looker web UI | [optional] 
**favorite_count** | **int** | Number of times favorited | [optional] 
**last_accessed_at** | **datetime** | Time that the Look was last accessed by any user | [optional] 
**content_favorite_id** | **int** | Content Favorite Id | [optional] 
**title** | **str** | Look Title | [optional] 
**user** | [**UserIdOnly**](UserIdOnly.md) | User | [optional] 
**query_id** | **int** | Query Id | [optional] 
**description** | **str** | Description | [optional] 
**short_url** | **str** | Short Url | [optional] 
**space** | [**SpaceBase**](SpaceBase.md) | Space of this Look | [optional] 
**public** | **bool** | Is Public | [optional] 
**public_slug** | **str** | Public Slug | [optional] 
**user_id** | **int** | User Id | [optional] 
**space_id** | **str** | Space Id | [optional] 
**model** | [**LookModel**](LookModel.md) | Model | [optional] 
**public_url** | **str** | Public Url | [optional] 
**embed_url** | **str** | Embed Url | [optional] 
**image_embed_url** | **str** | Image Embed Url | [optional] 
**google_spreadsheet_formula** | **str** | Google Spreadsheet Formula | [optional] 
**excel_file_url** | **str** | Excel File Url | [optional] 
**created_at** | **datetime** | Time that the Look was created. | [optional] 
**deleted_at** | **datetime** | Time that the Look was deleted. | [optional] 
**updated_at** | **datetime** | Time that the Look was updated. | [optional] 
**last_updater_id** | **int** | Id of User that last updated the look. | [optional] 
**deleter_id** | **int** | Id of User that deleted the look. | [optional] 
**deleted** | **bool** | Whether or not a look is deleted. | [optional] 
**last_viewed_at** | **datetime** | Time last viewed in the Looker web UI | [optional] 
**is_run_on_load** | **bool** | auto-run query when Look viewed | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


