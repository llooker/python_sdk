# LDAPUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Primary email address | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**ldap_id** | **str** | LDAP&#39;s Unique ID for the user | [optional] 
**all_emails** | **list[str]** | Array of user&#39;s email addresses and aliases for use in migration | [optional] 
**ldap_dn** | **str** | LDAP&#39;s distinguished name for the user record | [optional] 
**roles** | **list[str]** | Array of user&#39;s roles (role names only) | [optional] 
**groups** | **list[str]** | Array of user&#39;s groups (group names only) | [optional] 
**attributes** | **dict(str, str)** | Dictionary of user&#39;s attrributes (name/value) | [optional] 
**url** | **str** | Link to ldap config | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


