# OIDCConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable/Disable OIDC authentication for the server | [optional] 
**identifier** | **str** | Relying Party Identifier (provided by OpenID Provider) | [optional] 
**secret** | **str** | (Write-Only) Relying Party Secret (provided by OpenID Provider) | [optional] 
**scopes** | **list[str]** | Array of scopes to request. | [optional] 
**issuer** | **str** | OpenID Provider Issuer | [optional] 
**audience** | **str** | OpenID Provider Audience | [optional] 
**authorization_endpoint** | **str** | OpenID Provider Authorization Url | [optional] 
**token_endpoint** | **str** | OpenID Provider Token Url | [optional] 
**userinfo_endpoint** | **str** | OpenID Provider User Information Url | [optional] 
**user_attribute_map_email** | **str** | Name of user record attributes used to indicate email address field | [optional] 
**user_attribute_map_first_name** | **str** | Name of user record attributes used to indicate first name | [optional] 
**user_attribute_map_last_name** | **str** | Name of user record attributes used to indicate last name | [optional] 
**new_user_migration_types** | **str** | Merge first-time oidc login to existing user account by email addresses. When a user logs in for the first time via oidc this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like &#39;email,ldap,google&#39; | [optional] 
**alternate_email_login_allowed** | **bool** | Allow alternate email-based login via &#39;/login/email&#39; for admins and for specified users with the &#39;login_special_email&#39; permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled. | [optional] 
**test_slug** | **str** | Slug to identify configurations that are created in order to run a OIDC config test | [optional] 
**modified_at** | **str** | When this config was last modified | [optional] 
**modified_by** | **str** | User id of user who last modified this config | [optional] 
**default_new_user_roles** | [**list[Role]**](Role.md) | (Read-only) Roles that will be applied to new users the first time they login via OIDC | [optional] 
**default_new_user_groups** | [**list[Group]**](Group.md) | (Read-only) Groups that will be applied to new users the first time they login via OIDC | [optional] 
**default_new_user_role_ids** | **list[int]** | (Write-Only) Array of ids of roles that will be applied to new users the first time they login via OIDC | [optional] 
**default_new_user_group_ids** | **list[int]** | (Write-Only) Array of ids of groups that will be applied to new users the first time they login via OIDC | [optional] 
**set_roles_from_groups** | **bool** | Set user roles in Looker based on groups from OIDC | [optional] 
**groups_attribute** | **str** | Name of user record attributes used to indicate groups. Used when &#39;groups_finder_type&#39; is set to &#39;grouped_attribute_values&#39; | [optional] 
**groups** | [**list[OIDCGroupRead]**](OIDCGroupRead.md) | (Read-only) Array of mappings between OIDC Groups and Looker Roles | [optional] 
**groups_with_role_ids** | [**list[OIDCGroupWrite]**](OIDCGroupWrite.md) | (Read/Write) Array of mappings between OIDC Groups and arrays of Looker Role ids | [optional] 
**auth_requires_role** | **bool** | Users will not be allowed to login at all unless a role for them is found in OIDC if set to true | [optional] 
**user_attributes** | [**list[OIDCUserAttributeRead]**](OIDCUserAttributeRead.md) | (Read-only) Array of mappings between OIDC User Attributes and Looker User Attributes | [optional] 
**user_attributes_with_ids** | [**list[OIDCUserAttributeWrite]**](OIDCUserAttributeWrite.md) | (Read/Write) Array of mappings between OIDC User Attributes and arrays of Looker User Attribute ids | [optional] 
**url** | **str** | Link to get this item | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


