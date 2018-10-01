# lookerapi.DashboardApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_dashboards**](DashboardApi.md#all_dashboards) | **GET** /dashboards | Get All Dashboards
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /dashboards | Create Dashboard
[**create_dashboard_prefetch**](DashboardApi.md#create_dashboard_prefetch) | **POST** /dashboards/{dashboard_id}/prefetch | Create Dashboard Prefetch
[**dashboard**](DashboardApi.md#dashboard) | **GET** /dashboards/{dashboard_id} | Get Dashboard
[**dashboard_prefetch**](DashboardApi.md#dashboard_prefetch) | **GET** /dashboards/{dashboard_id}/prefetch | Get Dashboard Prefetch
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_id} | Delete Dashboard
[**search_dashboards**](DashboardApi.md#search_dashboards) | **GET** /dashboards/search | Search Dashboards
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PATCH** /dashboards/{dashboard_id} | Update Dashboard


# **all_dashboards**
> list[DashboardBase] all_dashboards(fields=fields)

Get All Dashboards

### Get information about all active dashboards.  Returns an array of **abbreviated dashboard objects**. Dashboards marked as deleted are excluded from this list.  Get the **full details** of a specific dashboard by id with [Dashboard](#!/Dashboard/dashboard)  Find **deleted dashboards** with [Search Dashboards](#!/Dashboard/search_dashboards) 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Dashboards
    api_response = api_instance.all_dashboards(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->all_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardBase]**](DashboardBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> Dashboard create_dashboard(body=body)

Create Dashboard

### Create a dashboard with the specified information  Creates a new dashboard object, returning the dashboard details, including the created id.  **Update** an existing dashboard with [Update Dashboard](#!/Dashboard/update_dashboard)  **Permanently delete** an existing dashboard with [Delete Dashboard](#!/Dashboard/delete_dashboard) 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
body = lookerapi.Dashboard() # Dashboard | Dashboard (optional)

try: 
    # Create Dashboard
    api_response = api_instance.create_dashboard(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| Dashboard | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_prefetch**
> PrefetchDashboardRequest create_dashboard_prefetch(dashboard_id, body=body)

Create Dashboard Prefetch

### Create a prefetch for a dashboard with the specified information.  **Deprecated** Use [DataGroups](#!/Datagroup) to manage cache invalidation of groups of queries. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
body = lookerapi.PrefetchDashboardRequest() # PrefetchDashboardRequest | Parameters for prefetch request (optional)

try: 
    # Create Dashboard Prefetch
    api_response = api_instance.create_dashboard_prefetch(dashboard_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard_prefetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **body** | [**PrefetchDashboardRequest**](PrefetchDashboardRequest.md)| Parameters for prefetch request | [optional] 

### Return type

[**PrefetchDashboardRequest**](PrefetchDashboardRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard**
> Dashboard dashboard(dashboard_id, fields=fields)

Get Dashboard

### Get information about the dashboard with the specified id  Returns the full details of the identified dashboard object  Get a **summary list** of all active dashboards with [All Dashboards](#!/Dashboard/all_dashboards)  **Search** for dashboards with [Search Dashboards](#!/Dashboard/search_dashboards) 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Dashboard
    api_response = api_instance.dashboard(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_prefetch**
> Prefetch dashboard_prefetch(dashboard_id, dashboard_filters=dashboard_filters)

Get Dashboard Prefetch

### Get a prefetch for a dashboard with the specified information.  **Deprecated** Use [DataGroups](#!/Datagroup) to manage cache invalidation of groups of queries. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
dashboard_filters = [lookerapi.PrefetchDashboardFilterValue()] # list[PrefetchDashboardFilterValue] | JSON encoded string of Dashboard filters that were applied to prefetch (optional)

try: 
    # Get Dashboard Prefetch
    api_response = api_instance.dashboard_prefetch(dashboard_id, dashboard_filters=dashboard_filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_prefetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **dashboard_filters** | [**list[PrefetchDashboardFilterValue]**](PrefetchDashboardFilterValue.md)| JSON encoded string of Dashboard filters that were applied to prefetch | [optional] 

### Return type

[**Prefetch**](Prefetch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> str delete_dashboard(dashboard_id)

Delete Dashboard

### Delete the dashboard with the specified id  Permanently **deletes** a dashboard. (The dashboard cannot be recovered after this operation.)  \"Soft\" delete or hide a dashboard by setting its `deleted` status to `True` with [Update Dashboard](#!/Dashboard/update_dashboard).  Note: When a dashboard is deleted in the UI, it is soft deleted. Use this API call to permanently remove it, if desired. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard

try: 
    # Delete Dashboard
    api_response = api_instance.delete_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboards**
> list[Dashboard] search_dashboards(fields=fields, id=id, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, deleted=deleted, user_id=user_id, view_count=view_count)

Search Dashboards

### Search all dashboards for matching criteria.  Returns an **array of dashboard objects** that match the specified search criteria.  The parameters `limit`, and `offset` are recommended for \"paging\" the returned results.  Get a **single dashboard** by id with [Dashboard](#!/Dashboard/dashboard) 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
fields = 'fields_example' # str | Requested fields. (optional)
id = 789 # int | Match dashboard id. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
limit = 789 # int | Number of results to return. (used with offset and takes priority over page and per_page) (optional)
offset = 789 # int | Number of results to skip before returning any. (used with limit and takes priority over page and per_page) (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
title = 'title_example' # str | Match Dashboard title. (optional)
description = 'description_example' # str | Match Dashboard description. (optional)
content_favorite_id = 789 # int | Filter on a content favorite id. (optional)
space_id = 'space_id_example' # str | Filter on a particular space. (optional)
deleted = 'deleted_example' # str | Filter on dashboards deleted status. (optional)
user_id = 'user_id_example' # str | Filter on dashboards created by a particular user. (optional)
view_count = 'view_count_example' # str | Filter on a particular value of view_count (optional)

try: 
    # Search Dashboards
    api_response = api_instance.search_dashboards(fields=fields, id=id, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, deleted=deleted, user_id=user_id, view_count=view_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->search_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **id** | **int**| Match dashboard id. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional] 
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **title** | **str**| Match Dashboard title. | [optional] 
 **description** | **str**| Match Dashboard description. | [optional] 
 **content_favorite_id** | **int**| Filter on a content favorite id. | [optional] 
 **space_id** | **str**| Filter on a particular space. | [optional] 
 **deleted** | **str**| Filter on dashboards deleted status. | [optional] 
 **user_id** | **str**| Filter on dashboards created by a particular user. | [optional] 
 **view_count** | **str**| Filter on a particular value of view_count | [optional] 

### Return type

[**list[Dashboard]**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id, body)

Update Dashboard

### Update the dashboard with the specified id  Changes simple (scalar) properties of the dashboard.  Change dashboard **elements** with [Update Dashboard Element](#!/Dashboard/update_dashboard_element)  Change dashboard **filters** with [Update Dashboard Filter](#!/Dashboard/update_dashboard_filter)  Change dashboard **layouts** with [Update Dashboard Layout](#!/Dashboard/update_dashboard_layout)  Change dashboard **layout components** with [Update Dashboard Layout Component](#!/Dashboard/update_dashboard_layout_components) 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
body = lookerapi.Dashboard() # Dashboard | Dashboard

try: 
    # Update Dashboard
    api_response = api_instance.update_dashboard(dashboard_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **body** | [**Dashboard**](Dashboard.md)| Dashboard | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

