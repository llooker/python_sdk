# swagger_client.SqlQueryApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sql_query**](SqlQueryApi.md#create_sql_query) | **POST** /sql_queries | Create SQL Runner Query
[**sql_query**](SqlQueryApi.md#sql_query) | **GET** /sql_queries/{slug} | Get SQL Runner Query


# **create_sql_query**
> SqlQuery create_sql_query(body)

Create SQL Runner Query

Create a SQL Runner query.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SqlQueryApi()
body = swagger_client.SqlQueryCreate() # SqlQueryCreate | SQL Runner Query

try: 
    # Create SQL Runner Query
    api_response = api_instance.create_sql_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlQueryApi->create_sql_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SqlQueryCreate**](SqlQueryCreate.md)| SQL Runner Query | 

### Return type

[**SqlQuery**](SqlQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_query**
> SqlQuery sql_query(slug)

Get SQL Runner Query

Get a SQL Runner query.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SqlQueryApi()
slug = 'slug_example' # str | slug of query

try: 
    # Get SQL Runner Query
    api_response = api_instance.sql_query(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlQueryApi->sql_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| slug of query | 

### Return type

[**SqlQuery**](SqlQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

