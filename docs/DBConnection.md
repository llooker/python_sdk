# DBConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connection. Also used as the unique identifier | [optional] 
**dialect** | [**Dialect**](Dialect.md) | (Read-only) SQL Dialect details | [optional] 
**snippets** | [**list[Snippet]**](Snippet.md) | SQL Runner snippets for this connection | [optional] 
**host** | **str** | Host name/address of server | [optional] 
**port** | **str** | Port number on server | [optional] 
**username** | **str** | Username for server authentication | [optional] 
**password** | **str** | (Write-Only) Password for server authentication | [optional] 
**certificate** | **str** | (Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect). | [optional] 
**file_type** | **str** | (Write-Only) Certificate keyfile type - .json or .p12 | [optional] 
**database** | **str** | Database name | [optional] 
**db_timezone** | **str** | Time zone of database | [optional] 
**query_timezone** | **str** | Timezone to use in queries | [optional] 
**schema** | **str** | Scheme name | [optional] 
**max_connections** | **int** | Maximum number of concurrent connection to use | [optional] 
**max_billing_gigabytes** | **str** | Maximum size of query in GBs (BigQuery only, can be a user_attribute name) | [optional] 
**ssl** | **bool** | Use SSL/TLS when connecting to server | [optional] 
**verify_ssl** | **bool** | Verify the SSL | [optional] 
**tmp_db_name** | **str** | Name of temporary database (if used) | [optional] 
**jdbc_additional_params** | **str** | Additional params to add to JDBC connection string | [optional] 
**pool_timeout** | **int** | Pool Timeout | [optional] 
**dialect_name** | **str** | (Read/Write) SQL Dialect name | [optional] 
**created_at** | **str** | Creation date for this connection | [optional] 
**user_id** | **str** | Id of user who last modified this connection configuration | [optional] 
**example** | **bool** | Is this an example connection | [optional] 
**user_db_credentials** | **bool** | (Limited access feature) Are per user db credentials enabled | [optional] 
**user_attribute_fields** | **list[str]** | Fields whose values map to user attribute names | [optional] 
**maintenance_cron** | **str** | Cron string specifying when maintenance such as PDT trigger checks and drops should be performed | [optional] 
**last_regen_at** | **str** | Unix timestamp at start of last completed PDT trigger check process | [optional] 
**last_reap_at** | **str** | Unix timestamp at start of last completed PDT reap process | [optional] 
**sql_runner_precache_tables** | **bool** | Precache tables in the SQL Runner | [optional] 
**after_connect_statements** | **str** | SQL statements (semicolon separated) to issue after connecting to the database. Requires &#x60;custom_after_connect_statements&#x60; license feature | [optional] 
**pdt_context_override** | [**DBConnectionOverride**](DBConnectionOverride.md) | db_connection_override for this connection in the &#x60;pdt&#x60; maintenance context | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


