# swagger_client.ContentApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_content_metadata_accesss**](ContentApi.md#all_content_metadata_accesss) | **GET** /content_metadata_access | Get All Content Metadata Accesss
[**all_content_metadatas**](ContentApi.md#all_content_metadatas) | **GET** /content_metadata | Get All Content Metadatas
[**content_favorite**](ContentApi.md#content_favorite) | **GET** /content_favorite/{content_favorite_id} | Get Favorite Content
[**content_metadata**](ContentApi.md#content_metadata) | **GET** /content_metadata/{content_metadata_id} | Get Content Metadata
[**create_content_favorite**](ContentApi.md#create_content_favorite) | **POST** /content_favorite | Create Favorite Content
[**create_content_metadata_access**](ContentApi.md#create_content_metadata_access) | **POST** /content_metadata_access | Create Content Metadata Access
[**delete_content_favorite**](ContentApi.md#delete_content_favorite) | **DELETE** /content_favorite/{content_favorite_id} | Delete Favorite Content
[**delete_content_metadata_access**](ContentApi.md#delete_content_metadata_access) | **DELETE** /content_metadata_access/{content_metadata_access_id} | Delete Content Metadata Access
[**search_content_favorites**](ContentApi.md#search_content_favorites) | **GET** /content_favorite/search | Search Favorite Contents
[**search_content_views**](ContentApi.md#search_content_views) | **GET** /content_view/search | Search Content Views
[**update_content_metadata**](ContentApi.md#update_content_metadata) | **PATCH** /content_metadata/{content_metadata_id} | Update Content Metadata
[**update_content_metadata_access**](ContentApi.md#update_content_metadata_access) | **PUT** /content_metadata_access/{content_metadata_access_id} | Update Content Metadata Access


# **all_content_metadata_accesss**
> list[ContentMetaGroupUser] all_content_metadata_accesss(content_metadata_id=content_metadata_id, fields=fields)

Get All Content Metadata Accesss

### All content metadata access records for a content metadata item. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_metadata_id = 789 # int | Id of content metadata (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Content Metadata Accesss
    api_response = api_instance.all_content_metadata_accesss(content_metadata_id=content_metadata_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->all_content_metadata_accesss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_metadata_id** | **int**| Id of content metadata | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ContentMetaGroupUser]**](ContentMetaGroupUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_content_metadatas**
> list[ContentMeta] all_content_metadatas(parent_id, fields=fields)

Get All Content Metadatas

### Get information about all content metadata in a space. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
parent_id = 789 # int | Parent space of content.
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Content Metadatas
    api_response = api_instance.all_content_metadatas(parent_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->all_content_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| Parent space of content. | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ContentMeta]**](ContentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_favorite**
> ContentFavorite content_favorite(content_favorite_id, fields=fields)

Get Favorite Content

### Get favorite content by its id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_favorite_id = 789 # int | Id of favorite content
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Favorite Content
    api_response = api_instance.content_favorite(content_favorite_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_favorite_id** | **int**| Id of favorite content | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ContentFavorite**](ContentFavorite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_metadata**
> ContentMeta content_metadata(content_metadata_id, fields=fields)

Get Content Metadata

### Get information about an individual content metadata record. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_metadata_id = 789 # int | Id of content metadata
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Content Metadata
    api_response = api_instance.content_metadata(content_metadata_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_metadata_id** | **int**| Id of content metadata | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ContentMeta**](ContentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_content_favorite**
> ContentFavorite create_content_favorite(body=body)

Create Favorite Content

### Create favorite content

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
body = swagger_client.ContentFavorite() # ContentFavorite | Favorite Content (optional)

try: 
    # Create Favorite Content
    api_response = api_instance.create_content_favorite(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->create_content_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentFavorite**](ContentFavorite.md)| Favorite Content | [optional] 

### Return type

[**ContentFavorite**](ContentFavorite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_content_metadata_access**
> ContentMetaGroupUser create_content_metadata_access(body=body)

Create Content Metadata Access

### Create content metadata access. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
body = swagger_client.ContentMetaGroupUser() # ContentMetaGroupUser | Content Metadata Access (optional)

try: 
    # Create Content Metadata Access
    api_response = api_instance.create_content_metadata_access(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->create_content_metadata_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentMetaGroupUser**](ContentMetaGroupUser.md)| Content Metadata Access | [optional] 

### Return type

[**ContentMetaGroupUser**](ContentMetaGroupUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_favorite**
> str delete_content_favorite(content_favorite_id)

Delete Favorite Content

### Delete favorite content

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_favorite_id = 789 # int | Id of favorite content

try: 
    # Delete Favorite Content
    api_response = api_instance.delete_content_favorite(content_favorite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->delete_content_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_favorite_id** | **int**| Id of favorite content | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_metadata_access**
> str delete_content_metadata_access(content_metadata_access_id)

Delete Content Metadata Access

### Remove content metadata access. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_metadata_access_id = 789 # int | Id of content metadata access

try: 
    # Delete Content Metadata Access
    api_response = api_instance.delete_content_metadata_access(content_metadata_access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->delete_content_metadata_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_metadata_access_id** | **int**| Id of content metadata access | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_content_favorites**
> list[ContentFavorite] search_content_favorites(user_id=user_id, limit=limit, offset=offset, sorts=sorts, fields=fields)

Search Favorite Contents

### Search Favorite Content 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
user_id = 789 # int | Match User Id (optional)
limit = 789 # int | Number of results to return. (used with offset) (optional)
offset = 789 # int | Number of results to skip before returning any. (used with limit) (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Search Favorite Contents
    api_response = api_instance.search_content_favorites(user_id=user_id, limit=limit, offset=offset, sorts=sorts, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->search_content_favorites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Match User Id | [optional] 
 **limit** | **int**| Number of results to return. (used with offset) | [optional] 
 **offset** | **int**| Number of results to skip before returning any. (used with limit) | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ContentFavorite]**](ContentFavorite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_content_views**
> list[ContentView] search_content_views(view_count=view_count, group_id=group_id, look_id=look_id, dashboard_id=dashboard_id, content_metadata_id=content_metadata_id, start_of_week_date=start_of_week_date, all_time=all_time, user_id=user_id, limit=limit, offset=offset, sorts=sorts, fields=fields)

Search Content Views

### Search Content View 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
view_count = 789 # int | Match view count (optional)
group_id = 789 # int | Match Group Id (optional)
look_id = 'look_id_example' # str | Match look_id (optional)
dashboard_id = 'dashboard_id_example' # str | Match dashboard_id (optional)
content_metadata_id = 789 # int | Match content metadata id (optional)
start_of_week_date = 'start_of_week_date_example' # str | Match start of week date (optional)
all_time = true # bool | True if only all time view records should be returned (optional)
user_id = 789 # int | Match user id (optional)
limit = 789 # int | Number of results to return. Use with `offset` to manage pagination of results (optional)
offset = 789 # int | Number of results to skip before returning data (optional)
sorts = 'sorts_example' # str | Fields to sort by (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Search Content Views
    api_response = api_instance.search_content_views(view_count=view_count, group_id=group_id, look_id=look_id, dashboard_id=dashboard_id, content_metadata_id=content_metadata_id, start_of_week_date=start_of_week_date, all_time=all_time, user_id=user_id, limit=limit, offset=offset, sorts=sorts, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->search_content_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_count** | **int**| Match view count | [optional] 
 **group_id** | **int**| Match Group Id | [optional] 
 **look_id** | **str**| Match look_id | [optional] 
 **dashboard_id** | **str**| Match dashboard_id | [optional] 
 **content_metadata_id** | **int**| Match content metadata id | [optional] 
 **start_of_week_date** | **str**| Match start of week date | [optional] 
 **all_time** | **bool**| True if only all time view records should be returned | [optional] 
 **user_id** | **int**| Match user id | [optional] 
 **limit** | **int**| Number of results to return. Use with &#x60;offset&#x60; to manage pagination of results | [optional] 
 **offset** | **int**| Number of results to skip before returning data | [optional] 
 **sorts** | **str**| Fields to sort by | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ContentView]**](ContentView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_metadata**
> ContentMeta update_content_metadata(content_metadata_id, body)

Update Content Metadata

### Move a piece of content. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_metadata_id = 789 # int | Id of content metadata
body = swagger_client.ContentMeta() # ContentMeta | Content Metadata

try: 
    # Update Content Metadata
    api_response = api_instance.update_content_metadata(content_metadata_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->update_content_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_metadata_id** | **int**| Id of content metadata | 
 **body** | [**ContentMeta**](ContentMeta.md)| Content Metadata | 

### Return type

[**ContentMeta**](ContentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_metadata_access**
> ContentMetaGroupUser update_content_metadata_access(content_metadata_access_id, body)

Update Content Metadata Access

### Update type of access for content metadata. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_metadata_access_id = 789 # int | Id of content metadata access
body = swagger_client.ContentMetaGroupUser() # ContentMetaGroupUser | Content Metadata Access

try: 
    # Update Content Metadata Access
    api_response = api_instance.update_content_metadata_access(content_metadata_access_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->update_content_metadata_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_metadata_access_id** | **int**| Id of content metadata access | 
 **body** | [**ContentMetaGroupUser**](ContentMetaGroupUser.md)| Content Metadata Access | 

### Return type

[**ContentMetaGroupUser**](ContentMetaGroupUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

