# swagger_client.SpaceApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_spaces**](SpaceApi.md#all_spaces) | **GET** /spaces | Get All Spaces
[**create_space**](SpaceApi.md#create_space) | **POST** /spaces | Create Space
[**delete_space**](SpaceApi.md#delete_space) | **DELETE** /spaces/{space_id} | Delete Space
[**search_spaces**](SpaceApi.md#search_spaces) | **GET** /spaces/search | Search Spaces
[**space**](SpaceApi.md#space) | **GET** /spaces/{space_id} | Get Space
[**space_ancestors**](SpaceApi.md#space_ancestors) | **GET** /spaces/{space_id}/ancestors | Get Space Ancestors
[**space_children**](SpaceApi.md#space_children) | **GET** /spaces/{space_id}/children | Get Space Children
[**space_children_search**](SpaceApi.md#space_children_search) | **GET** /spaces/{space_id}/children/search | Search Space Children
[**space_dashboards**](SpaceApi.md#space_dashboards) | **GET** /spaces/{space_id}/dashboards | Get Space Dashboards
[**space_looks**](SpaceApi.md#space_looks) | **GET** /spaces/{space_id}/looks | Get Space Looks
[**space_parent**](SpaceApi.md#space_parent) | **GET** /spaces/{space_id}/parent | Get Space Parent
[**update_space**](SpaceApi.md#update_space) | **PATCH** /spaces/{space_id} | Update Space


# **all_spaces**
> list[SpaceBase] all_spaces(fields=fields)

Get All Spaces

### Get information about all spaces.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Spaces
    api_response = api_instance.all_spaces(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->all_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[SpaceBase]**](SpaceBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> Space create_space(body=body)

Create Space

### Create a space with specified information.  Caller must have permission to edit the parent space and to create spaces, otherwise the request returns 404 Not Found. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
body = swagger_client.Space() # Space | Space (optional)

try: 
    # Create Space
    api_response = api_instance.create_space(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->create_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Space**](Space.md)| Space | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_space**
> str delete_space(space_id)

Delete Space

### Delete the space with a specific id including any children spaces. **DANGER** this will delete all looks and dashboards in the space. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space

try: 
    # Delete Space
    api_response = api_instance.delete_space(space_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->delete_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_spaces**
> list[Space] search_spaces(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, name=name, id=id, parent_id=parent_id, creator_id=creator_id)

Search Spaces

Search for spaces by creator id, parent id, name, etc

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
limit = 789 # int | Number of results to return. (used with offset and takes priority over page and per_page) (optional)
offset = 789 # int | Number of results to skip before returning any. (used with limit and takes priority over page and per_page) (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
name = 'name_example' # str | Match Space title. (optional)
id = 789 # int | Match Space id (optional)
parent_id = 'parent_id_example' # str | Filter on a children of a particular space. (optional)
creator_id = 'creator_id_example' # str | Filter on dashboards created by a particular user. (optional)

try: 
    # Search Spaces
    api_response = api_instance.search_spaces(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, name=name, id=id, parent_id=parent_id, creator_id=creator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->search_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional] 
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **name** | **str**| Match Space title. | [optional] 
 **id** | **int**| Match Space id | [optional] 
 **parent_id** | **str**| Filter on a children of a particular space. | [optional] 
 **creator_id** | **str**| Filter on dashboards created by a particular user. | [optional] 

### Return type

[**list[Space]**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space**
> Space space(space_id, fields=fields)

Get Space

### Get information about the space with a specific id.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Space
    api_response = api_instance.space(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_ancestors**
> list[Space] space_ancestors(space_id, fields=fields)

Get Space Ancestors

### Get the ancestors of a space

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Space Ancestors
    api_response = api_instance.space_ancestors(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Space]**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_children**
> list[Space] space_children(space_id, fields=fields, page=page, per_page=per_page, sorts=sorts)

Get Space Children

### Get the children of a space.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # Get Space Children
    api_response = api_instance.space_children(space_id, fields=fields, page=page, per_page=per_page, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**list[Space]**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_children_search**
> list[Space] space_children_search(space_id, fields=fields, sorts=sorts, name=name)

Search Space Children

### Search the children of a space

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
name = 'name_example' # str | Match Space name. (optional)

try: 
    # Search Space Children
    api_response = api_instance.space_children_search(space_id, fields=fields, sorts=sorts, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_children_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **name** | **str**| Match Space name. | [optional] 

### Return type

[**list[Space]**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_dashboards**
> list[Dashboard] space_dashboards(space_id, fields=fields)

Get Space Dashboards

### Get the dashboards in a space

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Space Dashboards
    api_response = api_instance.space_dashboards(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Dashboard]**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_looks**
> list[LookWithQuery] space_looks(space_id, fields=fields)

Get Space Looks

### Get the looks in a space

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Space Looks
    api_response = api_instance.space_looks(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_looks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[LookWithQuery]**](LookWithQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_parent**
> Space space_parent(space_id, fields=fields)

Get Space Parent

### Get the parent of a space

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Space Parent
    api_response = api_instance.space_parent(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->space_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_space**
> Space update_space(space_id, body)

Update Space

### Update the space with a specific id.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
space_id = 'space_id_example' # str | Id of space
body = swagger_client.Space() # Space | Space

try: 
    # Update Space
    api_response = api_instance.update_space(space_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->update_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **body** | [**Space**](Space.md)| Space | 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

