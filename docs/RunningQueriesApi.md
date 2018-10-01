# lookerapi.RunningQueriesApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_running_queries**](RunningQueriesApi.md#all_running_queries) | **GET** /running_queries | Get All Running Queries
[**kill_query**](RunningQueriesApi.md#kill_query) | **DELETE** /running_queries/{query_task_id} | Kill Running Query


# **all_running_queries**
> list[RunningQueries] all_running_queries()

Get All Running Queries

Get information about all running queries. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RunningQueriesApi()

try: 
    # Get All Running Queries
    api_response = api_instance.all_running_queries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningQueriesApi->all_running_queries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RunningQueries]**](RunningQueries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_query**
> str kill_query(query_task_id)

Kill Running Query

Kill a query with a specific query_task_id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.RunningQueriesApi()
query_task_id = 'query_task_id_example' # str | Query task id.

try: 
    # Kill Running Query
    api_response = api_instance.kill_query(query_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunningQueriesApi->kill_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_task_id** | **str**| Query task id. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

