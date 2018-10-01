# swagger_client.DatagroupApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_datagroups**](DatagroupApi.md#all_datagroups) | **GET** /datagroups | Get All Datagroups
[**datagroup**](DatagroupApi.md#datagroup) | **GET** /datagroups/{datagroup_id} | Get Datagroup
[**update_datagroup**](DatagroupApi.md#update_datagroup) | **PATCH** /datagroups/{datagroup_id} | Update Datagroup


# **all_datagroups**
> list[Datagroup] all_datagroups()

Get All Datagroups

### Get information about all datagroups. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatagroupApi()

try: 
    # Get All Datagroups
    api_response = api_instance.all_datagroups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatagroupApi->all_datagroups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Datagroup]**](Datagroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datagroup**
> Datagroup datagroup(datagroup_id)

Get Datagroup

### Get information about a datagroup. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatagroupApi()
datagroup_id = 'datagroup_id_example' # str | ID of datagroup.

try: 
    # Get Datagroup
    api_response = api_instance.datagroup(datagroup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatagroupApi->datagroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datagroup_id** | **str**| ID of datagroup. | 

### Return type

[**Datagroup**](Datagroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datagroup**
> Datagroup update_datagroup(datagroup_id, body)

Update Datagroup

### Update a datagroup using the specified params. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatagroupApi()
datagroup_id = 'datagroup_id_example' # str | ID of datagroup.
body = swagger_client.Datagroup() # Datagroup | Datagroup

try: 
    # Update Datagroup
    api_response = api_instance.update_datagroup(datagroup_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatagroupApi->update_datagroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datagroup_id** | **str**| ID of datagroup. | 
 **body** | [**Datagroup**](Datagroup.md)| Datagroup | 

### Return type

[**Datagroup**](Datagroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

