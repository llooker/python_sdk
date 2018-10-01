# lookerapi.RoleApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_model_sets**](RoleApi.md#all_model_sets) | **GET** /model_sets | Get All Model Sets
[**all_permission_sets**](RoleApi.md#all_permission_sets) | **GET** /permission_sets | Get All Permission Sets
[**all_permissions**](RoleApi.md#all_permissions) | **GET** /permissions | Get All Permissions
[**all_roles**](RoleApi.md#all_roles) | **GET** /roles | Get All Roles
[**create_model_set**](RoleApi.md#create_model_set) | **POST** /model_sets | Create Model Set
[**create_permission_set**](RoleApi.md#create_permission_set) | **POST** /permission_sets | Create Permission Set
[**create_role**](RoleApi.md#create_role) | **POST** /roles | Create Role
[**delete_model_set**](RoleApi.md#delete_model_set) | **DELETE** /model_sets/{model_set_id} | Delete Model Set
[**delete_permission_set**](RoleApi.md#delete_permission_set) | **DELETE** /permission_sets/{permission_set_id} | Delete Permission Set
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{role_id} | Delete Role
[**model_set**](RoleApi.md#model_set) | **GET** /model_sets/{model_set_id} | Get Model Set
[**permission_set**](RoleApi.md#permission_set) | **GET** /permission_sets/{permission_set_id} | Get Permission Set
[**role**](RoleApi.md#role) | **GET** /roles/{role_id} | Get Role
[**role_groups**](RoleApi.md#role_groups) | **GET** /roles/{role_id}/groups | Get Role Groups
[**role_users**](RoleApi.md#role_users) | **GET** /roles/{role_id}/users | Get Role Users
[**set_role_groups**](RoleApi.md#set_role_groups) | **PUT** /roles/{role_id}/groups | Update Role Groups
[**set_role_users**](RoleApi.md#set_role_users) | **PUT** /roles/{role_id}/users | Update Role Users
[**update_model_set**](RoleApi.md#update_model_set) | **PATCH** /model_sets/{model_set_id} | Update Model Set
[**update_permission_set**](RoleApi.md#update_permission_set) | **PATCH** /permission_sets/{permission_set_id} | Update Permission Set
[**update_role**](RoleApi.md#update_role) | **PATCH** /roles/{role_id} | Update Role


# **all_model_sets**
> list[ModelSet] all_model_sets(fields=fields)

Get All Model Sets

### Get information about all model sets. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Model Sets
    api_response = api_instance.all_model_sets(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->all_model_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ModelSet]**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_permission_sets**
> list[PermissionSet] all_permission_sets(fields=fields)

Get All Permission Sets

### Get information about all permission sets. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Permission Sets
    api_response = api_instance.all_permission_sets(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->all_permission_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[PermissionSet]**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_permissions**
> list[Permission] all_permissions()

Get All Permissions

### Get all supported permissions. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()

try: 
    # Get All Permissions
    api_response = api_instance.all_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->all_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Permission]**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_roles**
> list[Role] all_roles(fields=fields, ids=ids)

Get All Roles

### Get information about all roles. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)
ids = [56] # list[int] | Optional list of ids to get specific roles. (optional)

try: 
    # Get All Roles
    api_response = api_instance.all_roles(fields=fields, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->all_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **ids** | [**list[int]**](int.md)| Optional list of ids to get specific roles. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_set**
> ModelSet create_model_set(body=body)

Create Model Set

### Create a model set with the specified information. Model sets are used by Roles. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
body = lookerapi.ModelSet() # ModelSet | ModelSet (optional)

try: 
    # Create Model Set
    api_response = api_instance.create_model_set(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_model_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelSet**](ModelSet.md)| ModelSet | [optional] 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permission_set**
> PermissionSet create_permission_set(body=body)

Create Permission Set

### Create a permission set with the specified information. Permission sets are used by Roles. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
body = lookerapi.PermissionSet() # PermissionSet | Permission Set (optional)

try: 
    # Create Permission Set
    api_response = api_instance.create_permission_set(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionSet**](PermissionSet.md)| Permission Set | [optional] 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> Role create_role(body=body)

Create Role

### Create a role with the specified information. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
body = lookerapi.Role() # Role | Role (optional)

try: 
    # Create Role
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| Role | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_set**
> str delete_model_set(model_set_id)

Delete Model Set

### Delete the model set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
model_set_id = 789 # int | id of model set

try: 
    # Delete Model Set
    api_response = api_instance.delete_model_set(model_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_model_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| id of model set | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_set**
> str delete_permission_set(permission_set_id)

Delete Permission Set

### Delete the permission set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
permission_set_id = 789 # int | Id of permission set

try: 
    # Delete Permission Set
    api_response = api_instance.delete_permission_set(permission_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| Id of permission set | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> str delete_role(role_id)

Delete Role

### Delete the role with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of role

try: 
    # Delete Role
    api_response = api_instance.delete_role(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_set**
> ModelSet model_set(model_set_id, fields=fields)

Get Model Set

### Get information about the model set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
model_set_id = 789 # int | Id of model set
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Model Set
    api_response = api_instance.model_set(model_set_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->model_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| Id of model set | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_set**
> PermissionSet permission_set(permission_set_id, fields=fields)

Get Permission Set

### Get information about the permission set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
permission_set_id = 789 # int | Id of permission set
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Permission Set
    api_response = api_instance.permission_set(permission_set_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| Id of permission set | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role**
> Role role(role_id)

Get Role

### Get information about the role with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of role

try: 
    # Get Role
    api_response = api_instance.role(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_groups**
> list[Group] role_groups(role_id, fields=fields)

Get Role Groups

### Get information about all the groups with the role that has a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of role
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Role Groups
    api_response = api_instance.role_groups(role_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->role_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_users**
> list[User] role_users(role_id, fields=fields, direct_association_only=direct_association_only)

Get Role Users

### Get information about all the users with the role that has a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)
direct_association_only = true # bool | Get only users associated directly with the role: exclude those only associated through groups. (optional)

try: 
    # Get Role Users
    api_response = api_instance.role_users(role_id, fields=fields, direct_association_only=direct_association_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 
 **direct_association_only** | **bool**| Get only users associated directly with the role: exclude those only associated through groups. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_groups**
> list[Group] set_role_groups(role_id, body)

Update Role Groups

### Set all groups for a role, removing all existing group associations from that role. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | Id of Role
body = [lookerapi.list[int]()] # list[int] | Array of Group Ids

try: 
    # Update Role Groups
    api_response = api_instance.set_role_groups(role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->set_role_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Id of Role | 
 **body** | **list[int]**| Array of Group Ids | 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_users**
> list[User] set_role_users(role_id, body)

Update Role Users

### Set all the users of the role with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of role
body = [lookerapi.list[int]()] # list[int] | array of user ids for role

try: 
    # Update Role Users
    api_response = api_instance.set_role_users(role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->set_role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 
 **body** | **list[int]**| array of user ids for role | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_set**
> ModelSet update_model_set(model_set_id, body)

Update Model Set

### Update information about the model set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
model_set_id = 789 # int | id of model set
body = lookerapi.ModelSet() # ModelSet | ModelSet

try: 
    # Update Model Set
    api_response = api_instance.update_model_set(model_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_model_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| id of model set | 
 **body** | [**ModelSet**](ModelSet.md)| ModelSet | 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_set**
> PermissionSet update_permission_set(permission_set_id, body)

Update Permission Set

### Update information about the permission set with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
permission_set_id = 789 # int | id of permission set
body = lookerapi.PermissionSet() # PermissionSet | Permission Set

try: 
    # Update Permission Set
    api_response = api_instance.update_permission_set(permission_set_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| id of permission set | 
 **body** | [**PermissionSet**](PermissionSet.md)| Permission Set | 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(role_id, body)

Update Role

### Update information about the role with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RoleApi()
role_id = 789 # int | id of role
body = lookerapi.Role() # Role | Role

try: 
    # Update Role
    api_response = api_instance.update_role(role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 
 **body** | [**Role**](Role.md)| Role | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

