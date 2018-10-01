# swagger_client.LookmlModelApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_lookml_models**](LookmlModelApi.md#all_lookml_models) | **GET** /lookml_models | Get All LookML Models
[**create_lookml_model**](LookmlModelApi.md#create_lookml_model) | **POST** /lookml_models | Create LookML Model
[**delete_lookml_model**](LookmlModelApi.md#delete_lookml_model) | **DELETE** /lookml_models/{lookml_model_name} | Delete LookML Model
[**lookml_model**](LookmlModelApi.md#lookml_model) | **GET** /lookml_models/{lookml_model_name} | Get LookML Model
[**lookml_model_explore**](LookmlModelApi.md#lookml_model_explore) | **GET** /lookml_models/{lookml_model_name}/explores/{explore_name} | Get LookML Model Explore
[**update_lookml_model**](LookmlModelApi.md#update_lookml_model) | **PATCH** /lookml_models/{lookml_model_name} | Update LookML Model


# **all_lookml_models**
> list[LookmlModel] all_lookml_models(fields=fields)

Get All LookML Models

### Get information about all lookml models. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All LookML Models
    api_response = api_instance.all_lookml_models(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->all_lookml_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[LookmlModel]**](LookmlModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lookml_model**
> LookmlModel create_lookml_model(body=body)

Create LookML Model

### Create a lookml model using the specified configuration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
body = swagger_client.LookmlModel() # LookmlModel | LookML Model (optional)

try: 
    # Create LookML Model
    api_response = api_instance.create_lookml_model(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->create_lookml_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookmlModel**](LookmlModel.md)| LookML Model | [optional] 

### Return type

[**LookmlModel**](LookmlModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lookml_model**
> str delete_lookml_model(lookml_model_name)

Delete LookML Model

### Delete a lookml model. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
lookml_model_name = 'lookml_model_name_example' # str | Name of lookml model.

try: 
    # Delete LookML Model
    api_response = api_instance.delete_lookml_model(lookml_model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->delete_lookml_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_model_name** | **str**| Name of lookml model. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookml_model**
> LookmlModel lookml_model(lookml_model_name, fields=fields)

Get LookML Model

### Get information about a lookml model. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
lookml_model_name = 'lookml_model_name_example' # str | Name of lookml model.
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get LookML Model
    api_response = api_instance.lookml_model(lookml_model_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->lookml_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_model_name** | **str**| Name of lookml model. | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookmlModel**](LookmlModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookml_model_explore**
> LookmlModelExplore lookml_model_explore(lookml_model_name, explore_name, fields=fields)

Get LookML Model Explore

### Get information about a lookml model explore. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
lookml_model_name = 'lookml_model_name_example' # str | Name of lookml model.
explore_name = 'explore_name_example' # str | Name of explore.
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get LookML Model Explore
    api_response = api_instance.lookml_model_explore(lookml_model_name, explore_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->lookml_model_explore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_model_name** | **str**| Name of lookml model. | 
 **explore_name** | **str**| Name of explore. | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookmlModelExplore**](LookmlModelExplore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lookml_model**
> LookmlModel update_lookml_model(lookml_model_name, body)

Update LookML Model

### Update a lookml model using the specified configuration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookmlModelApi()
lookml_model_name = 'lookml_model_name_example' # str | Name of lookml model.
body = swagger_client.LookmlModel() # LookmlModel | LookML Model

try: 
    # Update LookML Model
    api_response = api_instance.update_lookml_model(lookml_model_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookmlModelApi->update_lookml_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_model_name** | **str**| Name of lookml model. | 
 **body** | [**LookmlModel**](LookmlModel.md)| LookML Model | 

### Return type

[**LookmlModel**](LookmlModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

