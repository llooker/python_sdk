# swagger_client.LookApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_looks**](LookApi.md#all_looks) | **GET** /looks | Get All Looks
[**create_look**](LookApi.md#create_look) | **POST** /looks | Create Look
[**delete_look**](LookApi.md#delete_look) | **DELETE** /looks/{look_id} | Delete Look
[**look**](LookApi.md#look) | **GET** /looks/{look_id} | Get Look
[**run_look**](LookApi.md#run_look) | **GET** /looks/{look_id}/run/{result_format} | Run Look
[**search_looks**](LookApi.md#search_looks) | **GET** /looks/search | Search Looks
[**update_look**](LookApi.md#update_look) | **PATCH** /looks/{look_id} | Update Look


# **all_looks**
> list[Look] all_looks(fields=fields)

Get All Looks

### Get all the looks.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Looks
    api_response = api_instance.all_looks(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->all_looks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Look]**](Look.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_look**
> LookWithQuery create_look(body=body, fields=fields)

Create Look

### Create a Look with specified information.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
body = swagger_client.LookWithQuery() # LookWithQuery | Look (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Look
    api_response = api_instance.create_look(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->create_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookWithQuery**](LookWithQuery.md)| Look | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookWithQuery**](LookWithQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_look**
> str delete_look(look_id)

Delete Look

### Delete the look with a specific id.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
look_id = 789 # int | Id of look

try: 
    # Delete Look
    api_response = api_instance.delete_look(look_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->delete_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **look**
> LookWithQuery look(look_id, fields=fields)

Get Look

### Get a Look.  Return detailed information about the Look and its associated Query.  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
look_id = 789 # int | Id of look
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Look
    api_response = api_instance.look(look_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookWithQuery**](LookWithQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_look**
> str run_look(look_id, result_format, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs)

Run Look

### Run a Look.  Runs a given look's query and returns the results in the requested format.  Suported formats:  | result_format | Description | :-----------: | :--- | | json | Plain json | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | md | Simple markdown | xlsx | MS Excel spreadsheet | sql | Returns the generated SQL rather than running the query | png | A PNG image of the visualization of the query | jpg | A JPG image of the visualization of the query   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
look_id = 789 # int | Id of look
result_format = 'result_format_example' # str | Format of result
limit = 789 # int | Row limit (may override the limit in the saved query). (optional)
apply_formatting = true # bool | Apply model-specified formatting to each result. (optional)
apply_vis = true # bool | Apply visualization options to results. (optional)
cache = true # bool | Get results from cache if available. (optional)
image_width = 789 # int | Render width for image formats. (optional)
image_height = 789 # int | Render height for image formats. (optional)
generate_drill_links = true # bool | Generate drill links (only applicable to 'json_detail' format. (optional)
force_production = true # bool | Force use of production models even if the user is in development mode. (optional)
cache_only = true # bool | Retrieve any results from cache even if the results have expired. (optional)
path_prefix = 'path_prefix_example' # str | Prefix to use for drill links (url encoded). (optional)
rebuild_pdts = true # bool | Rebuild PDTS used in query. (optional)
server_table_calcs = true # bool | Perform table calculations on query results (optional)

try: 
    # Run Look
    api_response = api_instance.run_look(look_id, result_format, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->run_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 
 **result_format** | **str**| Format of result | 
 **limit** | **int**| Row limit (may override the limit in the saved query). | [optional] 
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional] 
 **apply_vis** | **bool**| Apply visualization options to results. | [optional] 
 **cache** | **bool**| Get results from cache if available. | [optional] 
 **image_width** | **int**| Render width for image formats. | [optional] 
 **image_height** | **int**| Render height for image formats. | [optional] 
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;json_detail&#39; format. | [optional] 
 **force_production** | **bool**| Force use of production models even if the user is in development mode. | [optional] 
 **cache_only** | **bool**| Retrieve any results from cache even if the results have expired. | [optional] 
 **path_prefix** | **str**| Prefix to use for drill links (url encoded). | [optional] 
 **rebuild_pdts** | **bool**| Rebuild PDTS used in query. | [optional] 
 **server_table_calcs** | **bool**| Perform table calculations on query results | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text, application/json, image/png, image/jpg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_looks**
> list[Look] search_looks(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, user_id=user_id, view_count=view_count)

Search Looks

Search looks.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
limit = 789 # int | Number of results to return. (used with offset and takes priority over page and per_page) (optional)
offset = 789 # int | Number of results to skip before returning any. (used with limit and takes priority over page and per_page) (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
title = 'title_example' # str | Match Look title. (optional)
description = 'description_example' # str | Match Look description. (optional)
content_favorite_id = 789 # int | Match content favorite id (optional)
space_id = 'space_id_example' # str | Filter on a particular space. (optional)
user_id = 'user_id_example' # str | Filter on dashboards created by a particular user. (optional)
view_count = 'view_count_example' # str | Filter on a particular value of view_count (optional)

try: 
    # Search Looks
    api_response = api_instance.search_looks(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, user_id=user_id, view_count=view_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->search_looks: %s\n" % e)
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
 **title** | **str**| Match Look title. | [optional] 
 **description** | **str**| Match Look description. | [optional] 
 **content_favorite_id** | **int**| Match content favorite id | [optional] 
 **space_id** | **str**| Filter on a particular space. | [optional] 
 **user_id** | **str**| Filter on dashboards created by a particular user. | [optional] 
 **view_count** | **str**| Filter on a particular value of view_count | [optional] 

### Return type

[**list[Look]**](Look.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_look**
> LookWithQuery update_look(look_id, body, fields=fields)

Update Look

### Update the Look with a specific id.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookApi()
look_id = 789 # int | Id of look
body = swagger_client.LookWithQuery() # LookWithQuery | Look
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Look
    api_response = api_instance.update_look(look_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookApi->update_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 
 **body** | [**LookWithQuery**](LookWithQuery.md)| Look | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookWithQuery**](LookWithQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

