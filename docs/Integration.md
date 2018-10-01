# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the integration. | [optional] 
**integration_hub_id** | **int** | ID of the integration hub. | [optional] 
**label** | **str** | Label for the integration. | [optional] 
**description** | **str** | Description of the integration. | [optional] 
**enabled** | **bool** | Whether the integration is available to users. | [optional] 
**params** | [**list[IntegrationParam]**](IntegrationParam.md) | Array of params for the integration. | [optional] 
**supported_formats** | **list[str]** | A list of data formats the integration supports. Valid values are: \&quot;txt\&quot;, \&quot;csv\&quot;, \&quot;inline_json\&quot;, \&quot;json\&quot;, \&quot;json_detail\&quot;, \&quot;xlsx\&quot;, \&quot;html\&quot;, \&quot;wysiwyg_pdf\&quot;, \&quot;assembled_pdf\&quot;, \&quot;wysiwyg_png\&quot;, \&quot;csv_zip\&quot;. | [optional] 
**supported_action_types** | **list[str]** | A list of action types the integration supports. Valid values are: \&quot;cell\&quot;, \&quot;query\&quot;, \&quot;dashboard\&quot;. | [optional] 
**supported_formattings** | **list[str]** | A list of formatting options the integration supports. Valid values are: \&quot;formatted\&quot;, \&quot;unformatted\&quot;. | [optional] 
**supported_visualization_formattings** | **list[str]** | A list of visualization formatting options the integration supports. Valid values are: \&quot;apply\&quot;, \&quot;noapply\&quot;. | [optional] 
**supported_download_settings** | **list[str]** | A list of streaming options the integration supports. Valid values are: \&quot;push\&quot;, \&quot;url\&quot;. | [optional] 
**icon_url** | **str** | URL to an icon for the integration. | [optional] 
**required_fields** | [**list[IntegrationRequiredField]**](IntegrationRequiredField.md) | A list of descriptions of required fields that this integration is compatible with. If there are multiple entries in this list, the integration requires more than one field. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


