# swagger_client.UserAttributeApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_user_attribute_group_values**](UserAttributeApi.md#all_user_attribute_group_values) | **GET** /user_attributes/{user_attribute_id}/group_values | Get User Attribute Group Values
[**all_user_attributes**](UserAttributeApi.md#all_user_attributes) | **GET** /user_attributes | Get All User Attributes
[**create_user_attribute**](UserAttributeApi.md#create_user_attribute) | **POST** /user_attributes | Create User Attribute
[**delete_user_attribute**](UserAttributeApi.md#delete_user_attribute) | **DELETE** /user_attributes/{user_attribute_id} | Delete User Attribute
[**set_user_attribute_group_values**](UserAttributeApi.md#set_user_attribute_group_values) | **POST** /user_attributes/{user_attribute_id}/group_values | Set User Attribute Group Values
[**update_user_attribute**](UserAttributeApi.md#update_user_attribute) | **PATCH** /user_attributes/{user_attribute_id} | Update User Attribute
[**user_attribute**](UserAttributeApi.md#user_attribute) | **GET** /user_attributes/{user_attribute_id} | Get User Attribute


# **all_user_attribute_group_values**
> list[UserAttributeGroupValue] all_user_attribute_group_values(user_attribute_id, fields=fields)

Get User Attribute Group Values

### Returns all values of a user attribute defined by user groups, in precedence order.  A user may be a member of multiple groups which define different values for a given user attribute. The order of group-values in the response determines precedence for selecting which group-value applies to a given user.  For more information, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values).  Results will only include groups that the caller's user account has permission to see. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
user_attribute_id = 789 # int | Id of user attribute
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get User Attribute Group Values
    api_response = api_instance.all_user_attribute_group_values(user_attribute_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->all_user_attribute_group_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_attribute_id** | **int**| Id of user attribute | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[UserAttributeGroupValue]**](UserAttributeGroupValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_attributes**
> list[UserAttribute] all_user_attributes(fields=fields, sorts=sorts)

Get All User Attributes

### Get information about all user attributes. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
fields = 'fields_example' # str | Requested fields. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # Get All User Attributes
    api_response = api_instance.all_user_attributes(fields=fields, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->all_user_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**list[UserAttribute]**](UserAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_attribute**
> UserAttribute create_user_attribute(body=body, fields=fields)

Create User Attribute

### Create a new user attribute. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
body = swagger_client.UserAttribute() # UserAttribute | User Attribute (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create User Attribute
    api_response = api_instance.create_user_attribute(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->create_user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAttribute**](UserAttribute.md)| User Attribute | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**UserAttribute**](UserAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_attribute**
> str delete_user_attribute(user_attribute_id)

Delete User Attribute

### Delete a user attribute (admin only). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
user_attribute_id = 789 # int | Id of user_attribute

try: 
    # Delete User Attribute
    api_response = api_instance.delete_user_attribute(user_attribute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->delete_user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_attribute_id** | **int**| Id of user_attribute | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_attribute_group_values**
> list[UserAttributeGroupValue] set_user_attribute_group_values(user_attribute_id, body)

Set User Attribute Group Values

### Define values for a user attribute across a set of groups, in priority order.  This function defines all values for a user attribute defined by user groups. This is a global setting, potentially affecting all users in the system. This function replaces any existing group value definitions for the indicated user attribute.  The value of a user attribute for a given user is determined by searching the following locations, in this order:  1. the user's account settings 2. the groups that the user is a member of 3. the default value of the user attribute, if any  The user may be a member of multiple groups which define different values for that user attribute. The order of items in the group_values parameter determines which group takes priority for that user. Lowest array index wins.  An alternate method to indicate the selection precedence of group-values is to assign numbers to the 'rank' property of each group-value object in the array. Lowest 'rank' value wins. If you use this technique, you must assign a rank value to every group-value object in the array.  To set a user attribute value for a single user, see [Set User Attribute User Value](#!/User/set_user_attribute_user_value). To set a user attribute value for all members of a group, see [Set User Attribute Group Value](#!/Group/update_user_attribute_group_value). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
user_attribute_id = 789 # int | Id of user attribute
body = [swagger_client.UserAttributeGroupValue()] # list[UserAttributeGroupValue] | Array of group values.

try: 
    # Set User Attribute Group Values
    api_response = api_instance.set_user_attribute_group_values(user_attribute_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->set_user_attribute_group_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_attribute_id** | **int**| Id of user attribute | 
 **body** | [**list[UserAttributeGroupValue]**](UserAttributeGroupValue.md)| Array of group values. | 

### Return type

[**list[UserAttributeGroupValue]**](UserAttributeGroupValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_attribute**
> UserAttribute update_user_attribute(user_attribute_id, body, fields=fields)

Update User Attribute

### Update a user attribute definition. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
user_attribute_id = 789 # int | Id of user attribute
body = swagger_client.UserAttribute() # UserAttribute | User Attribute
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update User Attribute
    api_response = api_instance.update_user_attribute(user_attribute_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->update_user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_attribute_id** | **int**| Id of user attribute | 
 **body** | [**UserAttribute**](UserAttribute.md)| User Attribute | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**UserAttribute**](UserAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_attribute**
> UserAttribute user_attribute(user_attribute_id, fields=fields)

Get User Attribute

### Get information about a user attribute. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserAttributeApi()
user_attribute_id = 789 # int | Id of user attribute
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get User Attribute
    api_response = api_instance.user_attribute(user_attribute_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAttributeApi->user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_attribute_id** | **int**| Id of user attribute | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**UserAttribute**](UserAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

