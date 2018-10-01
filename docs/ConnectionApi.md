# swagger_client.ConnectionApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_connections**](ConnectionApi.md#all_connections) | **GET** /connections | Get All Connections
[**all_dialect_infos**](ConnectionApi.md#all_dialect_infos) | **GET** /dialect_info | Get All Dialect Infos
[**connection**](ConnectionApi.md#connection) | **GET** /connections/{connection_name} | Get Connection
[**create_connection**](ConnectionApi.md#create_connection) | **POST** /connections | Create Connection
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connections/{connection_name} | Delete Connection
[**delete_connection_override**](ConnectionApi.md#delete_connection_override) | **DELETE** /connections/{connection_name}/connection_override/{override_context} | Delete Connection
[**test_connection**](ConnectionApi.md#test_connection) | **PUT** /connections/{connection_name}/test | Test Connection
[**test_connection_config**](ConnectionApi.md#test_connection_config) | **PUT** /connections/test | Test Connection Configuration
[**update_connection**](ConnectionApi.md#update_connection) | **PATCH** /connections/{connection_name} | Update Connection


# **all_connections**
> list[DBConnection] all_connections(fields=fields)

Get All Connections

### Get information about all connections. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Connections
    api_response = api_instance.all_connections(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->all_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DBConnection]**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_dialect_infos**
> list[DialectInfo] all_dialect_infos(fields=fields)

Get All Dialect Infos

### Get information about all dialects. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Dialect Infos
    api_response = api_instance.all_dialect_infos(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->all_dialect_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DialectInfo]**](DialectInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connection**
> DBConnection connection(connection_name, fields=fields)

Get Connection

### Get information about a connection. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Connection
    api_response = api_instance.connection(connection_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> DBConnection create_connection(body=body)

Create Connection

### Create a connection using the specified configuration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.DBConnection() # DBConnection | Connection (optional)

try: 
    # Create Connection
    api_response = api_instance.create_connection(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DBConnection**](DBConnection.md)| Connection | [optional] 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> str delete_connection(connection_name)

Delete Connection

### Delete a connection. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection

try: 
    # Delete Connection
    api_response = api_instance.delete_connection(connection_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_override**
> str delete_connection_override(connection_name, override_context)

Delete Connection

### Delete a connection override. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
override_context = 'override_context_example' # str | Context of connection override

try: 
    # Delete Connection
    api_response = api_instance.delete_connection_override(connection_name, override_context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->delete_connection_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **override_context** | **str**| Context of connection override | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection**
> list[DBConnectionTestResult] test_connection(connection_name, tests=tests)

Test Connection

### Test an existing connection.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
tests = ['tests_example'] # list[str] | Array of names of tests to run (optional)

try: 
    # Test Connection
    api_response = api_instance.test_connection(connection_name, tests=tests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->test_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **tests** | [**list[str]**](str.md)| Array of names of tests to run | [optional] 

### Return type

[**list[DBConnectionTestResult]**](DBConnectionTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_config**
> list[DBConnectionTestResult] test_connection_config(body=body, tests=tests)

Test Connection Configuration

### Test a connection configuration.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.DBConnection() # DBConnection | Connection (optional)
tests = ['tests_example'] # list[str] | Array of names of tests to run (optional)

try: 
    # Test Connection Configuration
    api_response = api_instance.test_connection_config(body=body, tests=tests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->test_connection_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DBConnection**](DBConnection.md)| Connection | [optional] 
 **tests** | [**list[str]**](str.md)| Array of names of tests to run | [optional] 

### Return type

[**list[DBConnectionTestResult]**](DBConnectionTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> DBConnection update_connection(connection_name, body)

Update Connection

### Update a connection using the specified configuration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
body = swagger_client.DBConnection() # DBConnection | Connection

try: 
    # Update Connection
    api_response = api_instance.update_connection(connection_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->update_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **body** | [**DBConnection**](DBConnection.md)| Connection | 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

