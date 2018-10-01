# DBConnectionOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context in which to override (&#x60;pdt&#x60; is the only allowed value) | [optional] 
**host** | **str** | Host name/address of server | [optional] 
**port** | **str** | Port number on server | [optional] 
**username** | **str** | Username for server authentication | [optional] 
**password** | **str** | (Write-Only) Password for server authentication | [optional] 
**has_password** | **bool** | Whether or not the password is overridden in this context | [optional] 
**certificate** | **str** | (Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect). | [optional] 
**file_type** | **str** | (Write-Only) Certificate keyfile type - .json or .p12 | [optional] 
**database** | **str** | Database name | [optional] 
**schema** | **str** | Scheme name | [optional] 
**jdbc_additional_params** | **str** | Additional params to add to JDBC connection string | [optional] 
**after_connect_statements** | **str** | SQL statements (semicolon separated) to issue after connecting to the database. Requires &#x60;custom_after_connect_statements&#x60; license feature | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


