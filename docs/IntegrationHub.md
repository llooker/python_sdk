# IntegrationHub

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the hub. | [optional] 
**url** | **str** | URL of the hub. | [optional] 
**label** | **str** | Label of the hub. | [optional] 
**official** | **bool** | Whether this hub is a first-party integration hub operated by Looker. | [optional] 
**fetch_error_message** | **str** | An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable. | [optional] 
**authorization_token** | **str** | (Write-Only) An authorization key that will be sent to the integration hub on every request. | [optional] 
**has_authorization_token** | **bool** | Whether the authorization_token is set for the hub. | [optional] 
**legal_agreement_signed** | **bool** | Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true. | [optional] 
**legal_agreement_required** | **bool** | Whether the legal terms for the integration hub are required before use. | [optional] 
**legal_agreement_text** | **str** | The legal agreement text for this integration hub. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


