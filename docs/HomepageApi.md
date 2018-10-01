# swagger_client.HomepageApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_homepage_items**](HomepageApi.md#all_homepage_items) | **GET** /homepage_items | Get All Homepage Items
[**all_homepage_sections**](HomepageApi.md#all_homepage_sections) | **GET** /homepage_sections | Get All Homepage sections
[**create_homepage_item**](HomepageApi.md#create_homepage_item) | **POST** /homepage_items | Create Homepage Item
[**create_homepage_section**](HomepageApi.md#create_homepage_section) | **POST** /homepage_sections | Create Homepage section
[**delete_homepage_item**](HomepageApi.md#delete_homepage_item) | **DELETE** /homepage_items/{homepage_item_id} | Delete Homepage Item
[**delete_homepage_section**](HomepageApi.md#delete_homepage_section) | **DELETE** /homepage_sections/{homepage_section_id} | Delete Homepage section
[**homepage_item**](HomepageApi.md#homepage_item) | **GET** /homepage_items/{homepage_item_id} | Get Homepage Item
[**homepage_section**](HomepageApi.md#homepage_section) | **GET** /homepage_sections/{homepage_section_id} | Get Homepage section
[**update_homepage_item**](HomepageApi.md#update_homepage_item) | **PATCH** /homepage_items/{homepage_item_id} | Update Homepage Item
[**update_homepage_section**](HomepageApi.md#update_homepage_section) | **PATCH** /homepage_sections/{homepage_section_id} | Update Homepage section


# **all_homepage_items**
> list[HomepageItem] all_homepage_items(fields=fields, sorts=sorts, homepage_section_id=homepage_section_id)

Get All Homepage Items

### Get information about all homepage items. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
fields = 'fields_example' # str | Requested fields. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
homepage_section_id = 'homepage_section_id_example' # str | Filter to a specific homepage section (optional)

try: 
    # Get All Homepage Items
    api_response = api_instance.all_homepage_items(fields=fields, sorts=sorts, homepage_section_id=homepage_section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->all_homepage_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **homepage_section_id** | **str**| Filter to a specific homepage section | [optional] 

### Return type

[**list[HomepageItem]**](HomepageItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_homepage_sections**
> list[HomepageSection] all_homepage_sections(fields=fields, sorts=sorts)

Get All Homepage sections

### Get information about all homepage sections. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
fields = 'fields_example' # str | Requested fields. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # Get All Homepage sections
    api_response = api_instance.all_homepage_sections(fields=fields, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->all_homepage_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**list[HomepageSection]**](HomepageSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_homepage_item**
> HomepageItem create_homepage_item(body=body, fields=fields)

Create Homepage Item

### Create a new homepage item. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
body = swagger_client.HomepageItem() # HomepageItem | Homepage Item (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Homepage Item
    api_response = api_instance.create_homepage_item(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->create_homepage_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HomepageItem**](HomepageItem.md)| Homepage Item | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageItem**](HomepageItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_homepage_section**
> HomepageSection create_homepage_section(body=body, fields=fields)

Create Homepage section

### Create a new homepage section. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
body = swagger_client.HomepageSection() # HomepageSection | Homepage section (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Homepage section
    api_response = api_instance.create_homepage_section(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->create_homepage_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HomepageSection**](HomepageSection.md)| Homepage section | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageSection**](HomepageSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_homepage_item**
> str delete_homepage_item(homepage_item_id)

Delete Homepage Item

### Delete a homepage item. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_item_id = 789 # int | Id of homepage_item

try: 
    # Delete Homepage Item
    api_response = api_instance.delete_homepage_item(homepage_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->delete_homepage_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_item_id** | **int**| Id of homepage_item | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_homepage_section**
> str delete_homepage_section(homepage_section_id)

Delete Homepage section

### Delete a homepage section. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_section_id = 789 # int | Id of homepage_section

try: 
    # Delete Homepage section
    api_response = api_instance.delete_homepage_section(homepage_section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->delete_homepage_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_section_id** | **int**| Id of homepage_section | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **homepage_item**
> HomepageItem homepage_item(homepage_item_id, fields=fields)

Get Homepage Item

### Get information about a homepage item. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_item_id = 789 # int | Id of homepage item
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Homepage Item
    api_response = api_instance.homepage_item(homepage_item_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->homepage_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_item_id** | **int**| Id of homepage item | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageItem**](HomepageItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **homepage_section**
> HomepageSection homepage_section(homepage_section_id, fields=fields)

Get Homepage section

### Get information about a homepage section. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_section_id = 789 # int | Id of homepage section
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Homepage section
    api_response = api_instance.homepage_section(homepage_section_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->homepage_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_section_id** | **int**| Id of homepage section | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageSection**](HomepageSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_homepage_item**
> HomepageItem update_homepage_item(homepage_item_id, body, fields=fields)

Update Homepage Item

### Update a homepage item definition. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_item_id = 789 # int | Id of homepage item
body = swagger_client.HomepageItem() # HomepageItem | Homepage Item
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Homepage Item
    api_response = api_instance.update_homepage_item(homepage_item_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->update_homepage_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_item_id** | **int**| Id of homepage item | 
 **body** | [**HomepageItem**](HomepageItem.md)| Homepage Item | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageItem**](HomepageItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_homepage_section**
> HomepageSection update_homepage_section(homepage_section_id, body, fields=fields)

Update Homepage section

### Update a homepage section definition. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomepageApi()
homepage_section_id = 789 # int | Id of homepage section
body = swagger_client.HomepageSection() # HomepageSection | Homepage section
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Update Homepage section
    api_response = api_instance.update_homepage_section(homepage_section_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomepageApi->update_homepage_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homepage_section_id** | **int**| Id of homepage section | 
 **body** | [**HomepageSection**](HomepageSection.md)| Homepage section | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**HomepageSection**](HomepageSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

