# swagger_client.UserApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_user_access_filters**](UserApi.md#all_user_access_filters) | **GET** /users/{user_id}/access_filters | Get All Access Filters
[**all_user_credentials_api3s**](UserApi.md#all_user_credentials_api3s) | **GET** /users/{user_id}/credentials_api3 | Get All API 3 Credentials
[**all_user_credentials_embeds**](UserApi.md#all_user_credentials_embeds) | **GET** /users/{user_id}/credentials_embed | Get All Embedding Credentials
[**all_user_sessions**](UserApi.md#all_user_sessions) | **GET** /users/{user_id}/sessions | Get All Web Login Sessions
[**all_users**](UserApi.md#all_users) | **GET** /users | Get All Users
[**create_user**](UserApi.md#create_user) | **POST** /users | Create User
[**create_user_access_filter**](UserApi.md#create_user_access_filter) | **POST** /users/{user_id}/access_filters | Create Access Filter
[**create_user_credentials_api**](UserApi.md#create_user_credentials_api) | **POST** /users/{user_id}/credentials_api | Create API Credential
[**create_user_credentials_api3**](UserApi.md#create_user_credentials_api3) | **POST** /users/{user_id}/credentials_api3 | Create API 3 Credential
[**create_user_credentials_email**](UserApi.md#create_user_credentials_email) | **POST** /users/{user_id}/credentials_email | Create Email/Password Credential
[**create_user_credentials_email_password_reset**](UserApi.md#create_user_credentials_email_password_reset) | **POST** /users/{user_id}/credentials_email/password_reset | Create Password Reset Token
[**create_user_credentials_totp**](UserApi.md#create_user_credentials_totp) | **POST** /users/{user_id}/credentials_totp | Create Two-Factor Credential
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete User
[**delete_user_access_filter**](UserApi.md#delete_user_access_filter) | **DELETE** /users/{user_id}/access_filters/{access_filter_id} | Delete Access Filter
[**delete_user_attribute_user_value**](UserApi.md#delete_user_attribute_user_value) | **DELETE** /users/{user_id}/attribute_values/{user_attribute_id} | Delete User Attribute User Value
[**delete_user_credentials_api**](UserApi.md#delete_user_credentials_api) | **DELETE** /users/{user_id}/credentials_api | Delete API Credential
[**delete_user_credentials_api3**](UserApi.md#delete_user_credentials_api3) | **DELETE** /users/{user_id}/credentials_api3/{credentials_api3_id} | Delete API 3 Credential
[**delete_user_credentials_email**](UserApi.md#delete_user_credentials_email) | **DELETE** /users/{user_id}/credentials_email | Delete Email/Password Credential
[**delete_user_credentials_embed**](UserApi.md#delete_user_credentials_embed) | **DELETE** /users/{user_id}/credentials_embed/{credentials_embed_id} | Delete Embedding Credential
[**delete_user_credentials_google**](UserApi.md#delete_user_credentials_google) | **DELETE** /users/{user_id}/credentials_google | Delete Google Auth Credential
[**delete_user_credentials_ldap**](UserApi.md#delete_user_credentials_ldap) | **DELETE** /users/{user_id}/credentials_ldap | Delete LDAP Credential
[**delete_user_credentials_looker_openid**](UserApi.md#delete_user_credentials_looker_openid) | **DELETE** /users/{user_id}/credentials_looker_openid | Delete Looker OpenId Credential
[**delete_user_credentials_oidc**](UserApi.md#delete_user_credentials_oidc) | **DELETE** /users/{user_id}/credentials_oidc | Delete OIDC Auth Credential
[**delete_user_credentials_saml**](UserApi.md#delete_user_credentials_saml) | **DELETE** /users/{user_id}/credentials_saml | Delete Saml Auth Credential
[**delete_user_credentials_totp**](UserApi.md#delete_user_credentials_totp) | **DELETE** /users/{user_id}/credentials_totp | Delete Two-Factor Credential
[**delete_user_session**](UserApi.md#delete_user_session) | **DELETE** /users/{user_id}/sessions/{session_id} | Delete Web Login Session
[**me**](UserApi.md#me) | **GET** /user | Get Current User
[**search_users**](UserApi.md#search_users) | **GET** /users/search | Search Users
[**search_users_names**](UserApi.md#search_users_names) | **GET** /users/search/names/{pattern} | Search User Names
[**set_user_attribute_user_value**](UserApi.md#set_user_attribute_user_value) | **PATCH** /users/{user_id}/attribute_values/{user_attribute_id} | Set User Attribute User Value
[**set_user_roles**](UserApi.md#set_user_roles) | **PUT** /users/{user_id}/roles | Set User Roles
[**update_user**](UserApi.md#update_user) | **PATCH** /users/{user_id} | Update User
[**update_user_access_filter**](UserApi.md#update_user_access_filter) | **PATCH** /users/{user_id}/access_filters/{access_filter_id} | Update Access Filter
[**update_user_credentials_email**](UserApi.md#update_user_credentials_email) | **PATCH** /users/{user_id}/credentials_email | Update Email/Password Credential
[**user**](UserApi.md#user) | **GET** /users/{user_id} | Get User by Id
[**user_access_filter**](UserApi.md#user_access_filter) | **GET** /users/{user_id}/access_filters/{access_filter_id} | Get Access Filter
[**user_attribute_user_values**](UserApi.md#user_attribute_user_values) | **GET** /users/{user_id}/attribute_values | Get User Attribute Values
[**user_credentials_api**](UserApi.md#user_credentials_api) | **GET** /users/{user_id}/credentials_api | Get API Credential
[**user_credentials_api3**](UserApi.md#user_credentials_api3) | **GET** /users/{user_id}/credentials_api3/{credentials_api3_id} | Get API 3 Credential
[**user_credentials_email**](UserApi.md#user_credentials_email) | **GET** /users/{user_id}/credentials_email | Get Email/Password Credential
[**user_credentials_embed**](UserApi.md#user_credentials_embed) | **GET** /users/{user_id}/credentials_embed/{credentials_embed_id} | Get Embedding Credential
[**user_credentials_google**](UserApi.md#user_credentials_google) | **GET** /users/{user_id}/credentials_google | Get Google Auth Credential
[**user_credentials_ldap**](UserApi.md#user_credentials_ldap) | **GET** /users/{user_id}/credentials_ldap | Get LDAP Credential
[**user_credentials_looker_openid**](UserApi.md#user_credentials_looker_openid) | **GET** /users/{user_id}/credentials_looker_openid | Get Looker OpenId Credential
[**user_credentials_oidc**](UserApi.md#user_credentials_oidc) | **GET** /users/{user_id}/credentials_oidc | Get OIDC Auth Credential
[**user_credentials_saml**](UserApi.md#user_credentials_saml) | **GET** /users/{user_id}/credentials_saml | Get Saml Auth Credential
[**user_credentials_totp**](UserApi.md#user_credentials_totp) | **GET** /users/{user_id}/credentials_totp | Get Two-Factor Credential
[**user_for_credential**](UserApi.md#user_for_credential) | **GET** /users/credential/{credential_type}/{credential_id} | Get User by Credential Id
[**user_roles**](UserApi.md#user_roles) | **GET** /users/{user_id}/roles | Get User Roles
[**user_session**](UserApi.md#user_session) | **GET** /users/{user_id}/sessions/{session_id} | Get Web Login Session


# **all_user_access_filters**
> list[AccessFilter] all_user_access_filters(user_id, fields=fields)

Get All Access Filters

### Access filter for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Access Filters
    api_response = api_instance.all_user_access_filters(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->all_user_access_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[AccessFilter]**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_credentials_api3s**
> list[CredentialsApi3] all_user_credentials_api3s(user_id, fields=fields)

Get All API 3 Credentials

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All API 3 Credentials
    api_response = api_instance.all_user_credentials_api3s(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->all_user_credentials_api3s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[CredentialsApi3]**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_credentials_embeds**
> list[CredentialsEmbed] all_user_credentials_embeds(user_id, fields=fields)

Get All Embedding Credentials

### Embed login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Embedding Credentials
    api_response = api_instance.all_user_credentials_embeds(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->all_user_credentials_embeds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[CredentialsEmbed]**](CredentialsEmbed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_sessions**
> list[Session] all_user_sessions(user_id, fields=fields)

Get All Web Login Sessions

### Web login session for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Web Login Sessions
    api_response = api_instance.all_user_sessions(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->all_user_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_users**
> list[User] all_users(fields=fields, page=page, per_page=per_page, sorts=sorts, ids=ids)

Get All Users

### Get information about all users. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
ids = [56] # list[int] | Optional list of ids to get specific users. (optional)

try: 
    # Get All Users
    api_response = api_instance.all_users(fields=fields, page=page, per_page=per_page, sorts=sorts, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **ids** | [**list[int]**](int.md)| Optional list of ids to get specific users. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(body=body, fields=fields)

Create User

### Create a user with the specified information. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.User() # User | User (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create User
    api_response = api_instance.create_user(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| User | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_access_filter**
> AccessFilter create_user_access_filter(user_id, body=body, fields=fields)

Create Access Filter

### Access filter for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = swagger_client.AccessFilter() # AccessFilter | Access Filter (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Access Filter
    api_response = api_instance.create_user_access_filter(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_access_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**AccessFilter**](AccessFilter.md)| Access Filter | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_api**
> CredentialsApi create_user_credentials_api(user_id, body=body)

Create API Credential

### Create API Credential. SUPPORT FOR THIS HAS BEEN REMOVED. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
body = swagger_client.CredentialsApi() # CredentialsApi | API Credential (optional)

try: 
    # Create API Credential
    api_response = api_instance.create_user_credentials_api(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_credentials_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **body** | [**CredentialsApi**](CredentialsApi.md)| API Credential | [optional] 

### Return type

[**CredentialsApi**](CredentialsApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_api3**
> CredentialsApi3 create_user_credentials_api3(user_id, body=body, fields=fields)

Create API 3 Credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = swagger_client.CredentialsApi3() # CredentialsApi3 | API 3 Credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create API 3 Credential
    api_response = api_instance.create_user_credentials_api3(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_credentials_api3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsApi3**](CredentialsApi3.md)| API 3 Credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi3**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_email**
> CredentialsEmail create_user_credentials_email(user_id, body=body, fields=fields)

Create Email/Password Credential

### Email/password login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = swagger_client.CredentialsEmail() # CredentialsEmail | Email/Password Credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Email/Password Credential
    api_response = api_instance.create_user_credentials_email(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_credentials_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsEmail**](CredentialsEmail.md)| Email/Password Credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_email_password_reset**
> CredentialsEmail create_user_credentials_email_password_reset(user_id, expires=expires, fields=fields)

Create Password Reset Token

### Create a password reset token. This will create a cryptographically secure random password reset token for the user. If the user already has a password reset token then this invalidates the old token and creates a new one. The token is expressed as the 'password_reset_url' of the user's email/password credential object. This takes an optional 'expires' param to indicate if the new token should be an expiring token. Tokens that expire are typically used for self-service password resets for existing users. Invitation emails for new users typically are not set to expire. The expire period is always 60 minutes when expires is enabled. This method can be called with an empty body. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
expires = true # bool | Expiring token. (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Password Reset Token
    api_response = api_instance.create_user_credentials_email_password_reset(user_id, expires=expires, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_credentials_email_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **expires** | **bool**| Expiring token. | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_totp**
> CredentialsTotp create_user_credentials_totp(user_id, body=body, fields=fields)

Create Two-Factor Credential

### Two-factor login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = swagger_client.CredentialsTotp() # CredentialsTotp | Two-Factor Credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Two-Factor Credential
    api_response = api_instance.create_user_credentials_totp(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_credentials_totp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsTotp**](CredentialsTotp.md)| Two-Factor Credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsTotp**](CredentialsTotp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> str delete_user(user_id)

Delete User

### Delete the user with a specific id.  **DANGER** this will delete the user and all looks and other information owned by the user. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user

try: 
    # Delete User
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_access_filter**
> str delete_user_access_filter(user_id, access_filter_id)

Delete Access Filter

### Access filter for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
access_filter_id = 789 # int | id of Access Filter

try: 
    # Delete Access Filter
    api_response = api_instance.delete_user_access_filter(user_id, access_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_access_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **access_filter_id** | **int**| id of Access Filter | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_attribute_user_value**
> delete_user_attribute_user_value(user_id, user_attribute_id)

Delete User Attribute User Value

### Delete a user attribute value from a user's account settings.  After the user attribute value is deleted from the user's account settings, subsequent requests for the user attribute value for this user will draw from the user's groups or the default value of the user attribute. See [Get User Attribute Values](#!/User/user_attribute_user_values) for more information about how user attribute values are resolved. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
user_attribute_id = 789 # int | Id of user attribute

try: 
    # Delete User Attribute User Value
    api_instance.delete_user_attribute_user_value(user_id, user_attribute_id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_attribute_user_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **user_attribute_id** | **int**| Id of user attribute | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_api**
> str delete_user_credentials_api(user_id)

Delete API Credential

### API login information for the specified user. This is for 'API Users' used for the 'old' query API. THIS SUPPORT HAS BEEN REMOVED.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete API Credential
    api_response = api_instance.delete_user_credentials_api(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_api3**
> str delete_user_credentials_api3(user_id, credentials_api3_id)

Delete API 3 Credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
credentials_api3_id = 789 # int | id of API 3 Credential

try: 
    # Delete API 3 Credential
    api_response = api_instance.delete_user_credentials_api3(user_id, credentials_api3_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_api3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **credentials_api3_id** | **int**| id of API 3 Credential | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_email**
> str delete_user_credentials_email(user_id)

Delete Email/Password Credential

### Email/password login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete Email/Password Credential
    api_response = api_instance.delete_user_credentials_email(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_embed**
> str delete_user_credentials_embed(user_id, credentials_embed_id)

Delete Embedding Credential

### Embed login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
credentials_embed_id = 789 # int | id of Embedding Credential

try: 
    # Delete Embedding Credential
    api_response = api_instance.delete_user_credentials_embed(user_id, credentials_embed_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_embed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **credentials_embed_id** | **int**| id of Embedding Credential | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_google**
> str delete_user_credentials_google(user_id)

Delete Google Auth Credential

### Google authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete Google Auth Credential
    api_response = api_instance.delete_user_credentials_google(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_ldap**
> str delete_user_credentials_ldap(user_id)

Delete LDAP Credential

### LDAP login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete LDAP Credential
    api_response = api_instance.delete_user_credentials_ldap(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_looker_openid**
> str delete_user_credentials_looker_openid(user_id)

Delete Looker OpenId Credential

### Looker Openid login information for the specified user. Used by Looker Analysts.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete Looker OpenId Credential
    api_response = api_instance.delete_user_credentials_looker_openid(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_looker_openid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_oidc**
> str delete_user_credentials_oidc(user_id)

Delete OIDC Auth Credential

### OpenID Connect (OIDC) authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete OIDC Auth Credential
    api_response = api_instance.delete_user_credentials_oidc(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_oidc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_saml**
> str delete_user_credentials_saml(user_id)

Delete Saml Auth Credential

### Saml authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete Saml Auth Credential
    api_response = api_instance.delete_user_credentials_saml(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_saml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_totp**
> str delete_user_credentials_totp(user_id)

Delete Two-Factor Credential

### Two-factor login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user

try: 
    # Delete Two-Factor Credential
    api_response = api_instance.delete_user_credentials_totp(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_credentials_totp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_session**
> str delete_user_session(user_id, session_id)

Delete Web Login Session

### Web login session for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
session_id = 789 # int | id of Web Login Session

try: 
    # Delete Web Login Session
    api_response = api_instance.delete_user_session(user_id, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **session_id** | **int**| id of Web Login Session | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> User me(fields=fields)

Get Current User

### Get information about the current user; i.e. the user account currently calling the API. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Current User
    api_response = api_instance.me(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> list[User] search_users(fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled, filter_or=filter_or, content_metadata_id=content_metadata_id, group_id=group_id)

Search Users

### Search users. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
id = 789 # int | Match User Id. (optional)
first_name = 'first_name_example' # str | Match First name. (optional)
last_name = 'last_name_example' # str | Match Last name. (optional)
verified_looker_employee = true # bool | Match Verified Looker employee. (optional)
email = 'email_example' # str | Match Email Address. (optional)
is_disabled = true # bool | Match Is disabled. (optional)
filter_or = true # bool | Do an OR search with parameters (optional)
content_metadata_id = 789 # int | Id of content metadata to which users must have access (optional)
group_id = 789 # int | Id of group of which users must be directly members (optional)

try: 
    # Search Users
    api_response = api_instance.search_users(fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled, filter_or=filter_or, content_metadata_id=content_metadata_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **id** | **int**| Match User Id. | [optional] 
 **first_name** | **str**| Match First name. | [optional] 
 **last_name** | **str**| Match Last name. | [optional] 
 **verified_looker_employee** | **bool**| Match Verified Looker employee. | [optional] 
 **email** | **str**| Match Email Address. | [optional] 
 **is_disabled** | **bool**| Match Is disabled. | [optional] 
 **filter_or** | **bool**| Do an OR search with parameters | [optional] 
 **content_metadata_id** | **int**| Id of content metadata to which users must have access | [optional] 
 **group_id** | **int**| Id of group of which users must be directly members | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_names**
> list[User] search_users_names(pattern, fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)

Search User Names

### Search users where first_name OR last_name OR email matches a string.  The results will be AND'd with any additional search parameters that are (optionally) included. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
pattern = 'pattern_example' # str | Pattern to match.
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
id = 789 # int | Match User Id. (optional)
first_name = 'first_name_example' # str | Match First name. (optional)
last_name = 'last_name_example' # str | Match Last name. (optional)
verified_looker_employee = true # bool | Match Verified Looker employee. (optional)
email = 'email_example' # str | Match Email Address. (optional)
is_disabled = true # bool | Match Is disabled. (optional)

try: 
    # Search User Names
    api_response = api_instance.search_users_names(pattern, fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->search_users_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**| Pattern to match. | 
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **id** | **int**| Match User Id. | [optional] 
 **first_name** | **str**| Match First name. | [optional] 
 **last_name** | **str**| Match Last name. | [optional] 
 **verified_looker_employee** | **bool**| Match Verified Looker employee. | [optional] 
 **email** | **str**| Match Email Address. | [optional] 
 **is_disabled** | **bool**| Match Is disabled. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_attribute_user_value**
> UserAttributeWithValue set_user_attribute_user_value(user_id, user_attribute_id, body)

Set User Attribute User Value

### Store a custom value for a user attribute in a user's account settings.  Per-user user attribute values take precedence over group or default values. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
user_attribute_id = 789 # int | Id of user attribute
body = swagger_client.UserAttributeWithValue() # UserAttributeWithValue | New attribute value for user.

try: 
    # Set User Attribute User Value
    api_response = api_instance.set_user_attribute_user_value(user_id, user_attribute_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_attribute_user_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **user_attribute_id** | **int**| Id of user attribute | 
 **body** | [**UserAttributeWithValue**](UserAttributeWithValue.md)| New attribute value for user. | 

### Return type

[**UserAttributeWithValue**](UserAttributeWithValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> list[Role] set_user_roles(user_id, body, fields=fields)

Set User Roles

### Set roles of the user with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = [swagger_client.list[int]()] # list[int] | array of roles ids for user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Set User Roles
    api_response = api_instance.set_user_roles(user_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | **list[int]**| array of roles ids for user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, body, fields=fields)

Update User

### Update information about the user with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
body = swagger_client.User() # User | User
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update User
    api_response = api_instance.update_user(user_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **body** | [**User**](User.md)| User | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_access_filter**
> AccessFilter update_user_access_filter(user_id, access_filter_id, body, fields=fields)

Update Access Filter

### Access filter for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
access_filter_id = 789 # int | id of Access Filter
body = swagger_client.AccessFilter() # AccessFilter | Access Filter
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Access Filter
    api_response = api_instance.update_user_access_filter(user_id, access_filter_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_access_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **access_filter_id** | **int**| id of Access Filter | 
 **body** | [**AccessFilter**](AccessFilter.md)| Access Filter | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_credentials_email**
> CredentialsEmail update_user_credentials_email(user_id, body, fields=fields)

Update Email/Password Credential

### Email/password login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
body = swagger_client.CredentialsEmail() # CredentialsEmail | Email/Password Credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Email/Password Credential
    api_response = api_instance.update_user_credentials_email(user_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_credentials_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsEmail**](CredentialsEmail.md)| Email/Password Credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> User user(user_id, fields=fields)

Get User by Id

### Get information about the user with a specific id.  If the caller is an admin or the caller is the user being specified, then full user information will be returned. Otherwise, a minimal 'public' variant of the user information will be returned. This contains The user name and avatar url, but no sensitive information. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get User by Id
    api_response = api_instance.user(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_access_filter**
> AccessFilter user_access_filter(user_id, access_filter_id, fields=fields)

Get Access Filter

### Access filter for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
access_filter_id = 789 # int | Id of Access Filter
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Access Filter
    api_response = api_instance.user_access_filter(user_id, access_filter_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_access_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **access_filter_id** | **int**| Id of Access Filter | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_attribute_user_values**
> list[UserAttributeWithValue] user_attribute_user_values(user_id, fields=fields, user_attribute_ids=user_attribute_ids, all_values=all_values, include_unset=include_unset)

Get User Attribute Values

### Get user attribute values for a given user.  Returns the values of specified user attributes (or all user attributes) for a certain user.  A value for each user attribute is searched for in the following locations, in this order: 1. in the user's account information 1. in groups that the user is a member of 1. the default value of the user attribute  If more than one group has a value defined for a user attribute, the group with the lowest rank wins.  The response will only include user attributes for which values were found. Use `include_unset=true` to include empty records for user attributes with no value.  The value of all hidden user attributes will be blank. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
fields = 'fields_example' # str | Requested fields. (optional)
user_attribute_ids = [56] # list[int] | Specific user attributes to request. Omit or leave blank to request all user attributes. (optional)
all_values = true # bool | If true, returns all values in the search path instead of just the first value found. Useful for debugging group precedence. (optional)
include_unset = true # bool | If true, returns an empty record for each requested attribute that has no user, group, or default value. (optional)

try: 
    # Get User Attribute Values
    api_response = api_instance.user_attribute_user_values(user_id, fields=fields, user_attribute_ids=user_attribute_ids, all_values=all_values, include_unset=include_unset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_attribute_user_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **fields** | **str**| Requested fields. | [optional] 
 **user_attribute_ids** | [**list[int]**](int.md)| Specific user attributes to request. Omit or leave blank to request all user attributes. | [optional] 
 **all_values** | **bool**| If true, returns all values in the search path instead of just the first value found. Useful for debugging group precedence. | [optional] 
 **include_unset** | **bool**| If true, returns an empty record for each requested attribute that has no user, group, or default value. | [optional] 

### Return type

[**list[UserAttributeWithValue]**](UserAttributeWithValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_api**
> CredentialsApi user_credentials_api(user_id, fields=fields)

Get API Credential

### API login information for the specified user. This is for 'API Users' used for the 'old' query API. THIS SUPPORT HAS BEEN REMOVED.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get API Credential
    api_response = api_instance.user_credentials_api(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi**](CredentialsApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_api3**
> CredentialsApi3 user_credentials_api3(user_id, credentials_api3_id, fields=fields)

Get API 3 Credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
credentials_api3_id = 789 # int | Id of API 3 Credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get API 3 Credential
    api_response = api_instance.user_credentials_api3(user_id, credentials_api3_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_api3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **credentials_api3_id** | **int**| Id of API 3 Credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi3**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_email**
> CredentialsEmail user_credentials_email(user_id, fields=fields)

Get Email/Password Credential

### Email/password login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Email/Password Credential
    api_response = api_instance.user_credentials_email(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_embed**
> CredentialsEmbed user_credentials_embed(user_id, credentials_embed_id, fields=fields)

Get Embedding Credential

### Embed login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
credentials_embed_id = 789 # int | Id of Embedding Credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Embedding Credential
    api_response = api_instance.user_credentials_embed(user_id, credentials_embed_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_embed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **credentials_embed_id** | **int**| Id of Embedding Credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmbed**](CredentialsEmbed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_google**
> CredentialsGoogle user_credentials_google(user_id, fields=fields)

Get Google Auth Credential

### Google authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Google Auth Credential
    api_response = api_instance.user_credentials_google(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsGoogle**](CredentialsGoogle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_ldap**
> CredentialsLDAP user_credentials_ldap(user_id, fields=fields)

Get LDAP Credential

### LDAP login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get LDAP Credential
    api_response = api_instance.user_credentials_ldap(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsLDAP**](CredentialsLDAP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_looker_openid**
> CredentialsLookerOpenid user_credentials_looker_openid(user_id, fields=fields)

Get Looker OpenId Credential

### Looker Openid login information for the specified user. Used by Looker Analysts.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Looker OpenId Credential
    api_response = api_instance.user_credentials_looker_openid(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_looker_openid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsLookerOpenid**](CredentialsLookerOpenid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_oidc**
> CredentialsOIDC user_credentials_oidc(user_id, fields=fields)

Get OIDC Auth Credential

### OpenID Connect (OIDC) authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get OIDC Auth Credential
    api_response = api_instance.user_credentials_oidc(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_oidc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsOIDC**](CredentialsOIDC.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_saml**
> CredentialsSaml user_credentials_saml(user_id, fields=fields)

Get Saml Auth Credential

### Saml authentication login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Saml Auth Credential
    api_response = api_instance.user_credentials_saml(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_saml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsSaml**](CredentialsSaml.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_totp**
> CredentialsTotp user_credentials_totp(user_id, fields=fields)

Get Two-Factor Credential

### Two-factor login information for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Two-Factor Credential
    api_response = api_instance.user_credentials_totp(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_credentials_totp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsTotp**](CredentialsTotp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_for_credential**
> User user_for_credential(credential_type, credential_id, fields=fields)

Get User by Credential Id

### Get information about the user with a credential of given type with specific id.  This is used to do things like find users by their embed external_user_id. Or, find the user with a given api3 client_id, etc. The 'credential_type' matchs the 'type' name of the various credential types. It must be one of the values listed in the table below. The 'credential_id' is your unique Id for the user and is specific to each type of credential.  An example using the Ruby sdk might look like:  `sdk.user_for_credential('embed', 'customer-4959425')`  This table shows the supported 'Credential Type' strings. The right column is for reference; it shows which field in the given credential type is actually searched when finding a user with the supplied 'credential_id'.  | Credential Types | Id Field Matched | | ---------------- | ---------------- | | email            | email            | | google           | google_user_id   | | saml             | saml_user_id     | | oidc             | oidc_user_id     | | ldap             | ldap_id          | | api              | token            | | api3             | client_id        | | embed            | external_user_id | | looker_openid    | email            |  NOTE: 'api' is the legacy Looker query API. The API you are currently looking at is 'api3'.  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
credential_type = 'credential_type_example' # str | Type name of credential
credential_id = 'credential_id_example' # str | Id of credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get User by Credential Id
    api_response = api_instance.user_for_credential(credential_type, credential_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_for_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_type** | **str**| Type name of credential | 
 **credential_id** | **str**| Id of credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_roles**
> list[Role] user_roles(user_id, fields=fields, direct_association_only=direct_association_only)

Get User Roles

### Get information about roles of the user with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)
direct_association_only = true # bool | Get only roles associated directly with the user: exclude those only associated through groups. (optional)

try: 
    # Get User Roles
    api_response = api_instance.user_roles(user_id, fields=fields, direct_association_only=direct_association_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 
 **direct_association_only** | **bool**| Get only roles associated directly with the user: exclude those only associated through groups. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_session**
> Session user_session(user_id, session_id, fields=fields)

Get Web Login Session

### Web login session for the specified user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_id = 789 # int | Id of user
session_id = 789 # int | Id of Web Login Session
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Web Login Session
    api_response = api_instance.user_session(user_id, session_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **session_id** | **int**| Id of Web Login Session | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

