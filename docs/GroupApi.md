# lookerapi.GroupApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_group**](GroupApi.md#add_group_group) | **POST** /groups/{group_id}/groups | Add a Group to Group
[**add_group_user**](GroupApi.md#add_group_user) | **POST** /groups/{group_id}/users | Add a User to Group
[**all_group_groups**](GroupApi.md#all_group_groups) | **GET** /groups/{group_id}/groups | Get All Groups in Group
[**all_group_users**](GroupApi.md#all_group_users) | **GET** /groups/{group_id}/users | Get All Users in Group
[**all_groups**](GroupApi.md#all_groups) | **GET** /groups | Get All Groups
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create Group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{group_id} | Delete Group
[**delete_group_from_group**](GroupApi.md#delete_group_from_group) | **DELETE** /groups/{group_id}/groups/{deleting_group_id} | Deletes a Group from Group
[**delete_group_user**](GroupApi.md#delete_group_user) | **DELETE** /groups/{group_id}/users/{user_id} | Remove a User from Group
[**delete_user_attribute_group_value**](GroupApi.md#delete_user_attribute_group_value) | **DELETE** /groups/{group_id}/attribute_values/{user_attribute_id} | Delete User Attribute Group Value
[**group**](GroupApi.md#group) | **GET** /groups/{group_id} | Get Group
[**update_group**](GroupApi.md#update_group) | **PATCH** /groups/{group_id} | Update Group
[**update_user_attribute_group_value**](GroupApi.md#update_user_attribute_group_value) | **PATCH** /groups/{group_id}/attribute_values/{user_attribute_id} | Set User Attribute Group Value


# **add_group_group**
> Group add_group_group(group_id, body=body)

Add a Group to Group

### Adds a new group to a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
body = lookerapi.GroupIdForGroupInclusion() # GroupIdForGroupInclusion | Group id to add (optional)

try: 
    # Add a Group to Group
    api_response = api_instance.add_group_group(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **body** | [**GroupIdForGroupInclusion**](GroupIdForGroupInclusion.md)| Group id to add | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_user**
> User add_group_user(group_id, body=body)

Add a User to Group

### Adds a new user to a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
body = lookerapi.GroupIdForGroupUserInclusion() # GroupIdForGroupUserInclusion | User id to add (optional)

try: 
    # Add a User to Group
    api_response = api_instance.add_group_user(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **body** | [**GroupIdForGroupUserInclusion**](GroupIdForGroupUserInclusion.md)| User id to add | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_group_groups**
> list[Group] all_group_groups(group_id, fields=fields)

Get All Groups in Group

### Get information about all the groups in a group 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Groups in Group
    api_response = api_instance.all_group_groups(group_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->all_group_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_group_users**
> list[User] all_group_users(group_id, fields=fields, page=page, per_page=per_page, sorts=sorts)

Get All Users in Group

### Get information about all the users directly included in a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # Get All Users in Group
    api_response = api_instance.all_group_users(group_id, fields=fields, page=page, per_page=per_page, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->all_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_groups**
> list[Group] all_groups(fields=fields, page=page, per_page=per_page, sorts=sorts, ids=ids, content_metadata_id=content_metadata_id, can_add_to_content_metadata=can_add_to_content_metadata)

Get All Groups

### Get information about all groups. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
ids = [56] # list[int] | Optional of ids to get specific groups. (optional)
content_metadata_id = 789 # int | Id of content metadata to which groups must have access. (optional)
can_add_to_content_metadata = true # bool | Select only groups that either can/cannot be given access to content. (optional)

try: 
    # Get All Groups
    api_response = api_instance.all_groups(fields=fields, page=page, per_page=per_page, sorts=sorts, ids=ids, content_metadata_id=content_metadata_id, can_add_to_content_metadata=can_add_to_content_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **ids** | [**list[int]**](int.md)| Optional of ids to get specific groups. | [optional] 
 **content_metadata_id** | **int**| Id of content metadata to which groups must have access. | [optional] 
 **can_add_to_content_metadata** | **bool**| Select only groups that either can/cannot be given access to content. | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body=body, fields=fields)

Create Group

### Creates a new group (admin only). 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
body = lookerapi.Group() # Group | Group (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Group
    api_response = api_instance.create_group(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| Group | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> str delete_group(group_id)

Delete Group

### Deletes a group (admin only). 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group

try: 
    # Delete Group
    api_response = api_instance.delete_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_from_group**
> delete_group_from_group(group_id, deleting_group_id)

Deletes a Group from Group

### Removes a group from a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
deleting_group_id = 789 # int | Id of group to delete

try: 
    # Deletes a Group from Group
    api_instance.delete_group_from_group(group_id, deleting_group_id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **deleting_group_id** | **int**| Id of group to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_user**
> delete_group_user(group_id, user_id)

Remove a User from Group

### Removes a user from a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
user_id = 789 # int | Id of user to remove from group

try: 
    # Remove a User from Group
    api_instance.delete_group_user(group_id, user_id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **user_id** | **int**| Id of user to remove from group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_attribute_group_value**
> delete_user_attribute_group_value(group_id, user_attribute_id)

Delete User Attribute Group Value

### Remove a user attribute value from a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
user_attribute_id = 789 # int | Id of user attribute

try: 
    # Delete User Attribute Group Value
    api_instance.delete_user_attribute_group_value(group_id, user_attribute_id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_user_attribute_group_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **user_attribute_id** | **int**| Id of user attribute | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group**
> Group group(group_id, fields=fields)

Get Group

### Get information about a group. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Group
    api_response = api_instance.group(group_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(group_id, body, fields=fields)

Update Group

### Updates the a group (admin only).

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
body = lookerapi.Group() # Group | Group
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Group
    api_response = api_instance.update_group(group_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **body** | [**Group**](Group.md)| Group | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_attribute_group_value**
> UserAttributeGroupValue update_user_attribute_group_value(group_id, user_attribute_id, body)

Set User Attribute Group Value

### Set the value of a user attribute for a group.  For information about how user attribute values are calculated, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values). 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.GroupApi()
group_id = 789 # int | Id of group
user_attribute_id = 789 # int | Id of user attribute
body = lookerapi.UserAttributeGroupValue() # UserAttributeGroupValue | New value for group.

try: 
    # Set User Attribute Group Value
    api_response = api_instance.update_user_attribute_group_value(group_id, user_attribute_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_user_attribute_group_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Id of group | 
 **user_attribute_id** | **int**| Id of user attribute | 
 **body** | [**UserAttributeGroupValue**](UserAttributeGroupValue.md)| New value for group. | 

### Return type

[**UserAttributeGroupValue**](UserAttributeGroupValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

