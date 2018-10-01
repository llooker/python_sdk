# ContentMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name or title of underlying content | [optional] 
**parent_id** | **int** | Id of Parent Content | [optional] 
**space_id** | **str** | Id of associated space when content_type is \&quot;space\&quot; | [optional] 
**dashboard_id** | **str** | Id of associated dashboard when content_type is \&quot;dashboard\&quot; | [optional] 
**look_id** | **int** | Id of associated look when content_type is \&quot;look\&quot; | [optional] 
**content_type** | **str** | Content Type (\&quot;dashboard\&quot;, \&quot;look\&quot;, or \&quot;space\&quot;) | [optional] 
**inherits** | **bool** | Whether content inherits its access levels from parent | [optional] 
**inheriting_id** | **int** | Id of Inherited Content | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


