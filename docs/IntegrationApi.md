# swagger_client.IntegrationApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_integration_hub_legal_agreement**](IntegrationApi.md#accept_integration_hub_legal_agreement) | **POST** /integration_hubs/{integration_hub_id}/accept_legal_agreement | Accept Integration Hub Legal Agreement
[**all_integration_hubs**](IntegrationApi.md#all_integration_hubs) | **GET** /integration_hubs | Get All Integration Hubs
[**all_integrations**](IntegrationApi.md#all_integrations) | **GET** /integrations | Get All Integrations
[**create_integration_hub**](IntegrationApi.md#create_integration_hub) | **POST** /integration_hubs | Create Integration Hub
[**delete_integration_hub**](IntegrationApi.md#delete_integration_hub) | **DELETE** /integration_hubs/{integration_hub_id} | Delete Integration Hub
[**fetch_integration_form**](IntegrationApi.md#fetch_integration_form) | **POST** /integrations/{integration_id}/form | Fetch Remote Integration Form
[**integration**](IntegrationApi.md#integration) | **GET** /integrations/{integration_id} | Get Integration
[**integration_hub**](IntegrationApi.md#integration_hub) | **GET** /integration_hubs/{integration_hub_id} | Get Integration Hub
[**update_integration**](IntegrationApi.md#update_integration) | **PATCH** /integrations/{integration_id} | Update Integration
[**update_integration_hub**](IntegrationApi.md#update_integration_hub) | **PATCH** /integration_hubs/{integration_hub_id} | Update Integration Hub


# **accept_integration_hub_legal_agreement**
> IntegrationHub accept_integration_hub_legal_agreement(integration_hub_id)

Accept Integration Hub Legal Agreement

Accepts the legal agreement for a given integration hub. This only works for integration hubs that have legal_agreement_required set to true and legal_agreement_signed set to false.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_hub_id = 789 # int | Id of integration_hub

try: 
    # Accept Integration Hub Legal Agreement
    api_response = api_instance.accept_integration_hub_legal_agreement(integration_hub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->accept_integration_hub_legal_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_hub_id** | **int**| Id of integration_hub | 

### Return type

[**IntegrationHub**](IntegrationHub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_integration_hubs**
> list[IntegrationHub] all_integration_hubs(fields=fields)

Get All Integration Hubs

### Get information about all Integration Hubs. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Integration Hubs
    api_response = api_instance.all_integration_hubs(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->all_integration_hubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[IntegrationHub]**](IntegrationHub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_integrations**
> list[Integration] all_integrations(fields=fields, integration_hub_id=integration_hub_id)

Get All Integrations

### Get information about all Integrations. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
fields = 'fields_example' # str | Requested fields. (optional)
integration_hub_id = 'integration_hub_id_example' # str | Filter to a specific provider (optional)

try: 
    # Get All Integrations
    api_response = api_instance.all_integrations(fields=fields, integration_hub_id=integration_hub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->all_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **integration_hub_id** | **str**| Filter to a specific provider | [optional] 

### Return type

[**list[Integration]**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_integration_hub**
> IntegrationHub create_integration_hub(body=body, fields=fields)

Create Integration Hub

### Create a new Integration Hub. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
body = swagger_client.IntegrationHub() # IntegrationHub | Integration Hub (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Integration Hub
    api_response = api_instance.create_integration_hub(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_integration_hub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationHub**](IntegrationHub.md)| Integration Hub | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**IntegrationHub**](IntegrationHub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_hub**
> str delete_integration_hub(integration_hub_id)

Delete Integration Hub

### Delete a Integration Hub. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_hub_id = 789 # int | Id of integration_hub

try: 
    # Delete Integration Hub
    api_response = api_instance.delete_integration_hub(integration_hub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_integration_hub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_hub_id** | **int**| Id of integration_hub | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_integration_form**
> DataActionForm fetch_integration_form(integration_id)

Fetch Remote Integration Form

Returns the Integration form for presentation to the user.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_id = 789 # int | Id of Integration

try: 
    # Fetch Remote Integration Form
    api_response = api_instance.fetch_integration_form(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->fetch_integration_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Id of Integration | 

### Return type

[**DataActionForm**](DataActionForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration**
> Integration integration(integration_id, fields=fields)

Get Integration

### Get information about a Integration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_id = 789 # int | Id of Integration
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Integration
    api_response = api_instance.integration(integration_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Id of Integration | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_hub**
> IntegrationHub integration_hub(integration_hub_id, fields=fields)

Get Integration Hub

### Get information about a Integration Hub. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_hub_id = 789 # int | Id of Integration Hub
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Integration Hub
    api_response = api_instance.integration_hub(integration_hub_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integration_hub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_hub_id** | **int**| Id of Integration Hub | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**IntegrationHub**](IntegrationHub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> Integration update_integration(integration_id, body, fields=fields)

Update Integration

### Update parameters on a Integration. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_id = 789 # int | Id of Integration
body = swagger_client.Integration() # Integration | Integration
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Integration
    api_response = api_instance.update_integration(integration_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **int**| Id of Integration | 
 **body** | [**Integration**](Integration.md)| Integration | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_hub**
> IntegrationHub update_integration_hub(integration_hub_id, body, fields=fields)

Update Integration Hub

### Update a Integration Hub definition. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
integration_hub_id = 789 # int | Id of Integration Hub
body = swagger_client.IntegrationHub() # IntegrationHub | Integration Hub
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Integration Hub
    api_response = api_instance.update_integration_hub(integration_hub_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration_hub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_hub_id** | **int**| Id of Integration Hub | 
 **body** | [**IntegrationHub**](IntegrationHub.md)| Integration Hub | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**IntegrationHub**](IntegrationHub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

