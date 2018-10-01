# lookerapi.ConfigApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_legacy_features**](ConfigApi.md#all_legacy_features) | **GET** /legacy_features | Get All Legacy Features
[**all_timezones**](ConfigApi.md#all_timezones) | **GET** /timezones | Get All Timezones
[**backup_configuration**](ConfigApi.md#backup_configuration) | **GET** /backup_configuration | Get Backup Configuration
[**legacy_feature**](ConfigApi.md#legacy_feature) | **GET** /legacy_features/{legacy_feature_id} | Get Legacy Feature
[**update_backup_configuration**](ConfigApi.md#update_backup_configuration) | **PATCH** /backup_configuration | Update Backup Configuration
[**update_legacy_feature**](ConfigApi.md#update_legacy_feature) | **PATCH** /legacy_features/{legacy_feature_id} | Update Legacy Feature
[**update_whitelabel_configuration**](ConfigApi.md#update_whitelabel_configuration) | **PUT** /whitelabel_configuration | Update Whitelabel configuration
[**versions**](ConfigApi.md#versions) | **GET** /versions | Get ApiVersion
[**whitelabel_configuration**](ConfigApi.md#whitelabel_configuration) | **GET** /whitelabel_configuration | Get Whitelabel configuration


# **all_legacy_features**
> list[LegacyFeature] all_legacy_features()

Get All Legacy Features

### Get all legacy features. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()

try: 
    # Get All Legacy Features
    api_response = api_instance.all_legacy_features()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->all_legacy_features: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LegacyFeature]**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_timezones**
> list[Timezone] all_timezones()

Get All Timezones

### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks). 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()

try: 
    # Get All Timezones
    api_response = api_instance.all_timezones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->all_timezones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Timezone]**](Timezone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_configuration**
> BackupConfiguration backup_configuration()

Get Backup Configuration

### Get the current Looker internal database backup configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()

try: 
    # Get Backup Configuration
    api_response = api_instance.backup_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->backup_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_feature**
> LegacyFeature legacy_feature(legacy_feature_id)

Get Legacy Feature

### Get information about the legacy feature with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
legacy_feature_id = 789 # int | id of legacy feature

try: 
    # Get Legacy Feature
    api_response = api_instance.legacy_feature(legacy_feature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->legacy_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_feature_id** | **int**| id of legacy feature | 

### Return type

[**LegacyFeature**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_backup_configuration**
> BackupConfiguration update_backup_configuration(body)

Update Backup Configuration

### Update the Looker internal database backup configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
body = lookerapi.BackupConfiguration() # BackupConfiguration | Options for Backup Configuration

try: 
    # Update Backup Configuration
    api_response = api_instance.update_backup_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_backup_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupConfiguration**](BackupConfiguration.md)| Options for Backup Configuration | 

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legacy_feature**
> LegacyFeature update_legacy_feature(legacy_feature_id, body)

Update Legacy Feature

### Update information about the legacy feature with a specific id. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
legacy_feature_id = 789 # int | id of legacy feature
body = lookerapi.LegacyFeature() # LegacyFeature | Legacy Feature

try: 
    # Update Legacy Feature
    api_response = api_instance.update_legacy_feature(legacy_feature_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_legacy_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_feature_id** | **int**| id of legacy feature | 
 **body** | [**LegacyFeature**](LegacyFeature.md)| Legacy Feature | 

### Return type

[**LegacyFeature**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_whitelabel_configuration**
> WhitelabelConfiguration update_whitelabel_configuration(body)

Update Whitelabel configuration

### Update the whitelabel configuration 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
body = lookerapi.WhitelabelConfiguration() # WhitelabelConfiguration | Whitelabel configuration

try: 
    # Update Whitelabel configuration
    api_response = api_instance.update_whitelabel_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_whitelabel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WhitelabelConfiguration**](WhitelabelConfiguration.md)| Whitelabel configuration | 

### Return type

[**WhitelabelConfiguration**](WhitelabelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions**
> ApiVersion versions(fields=fields)

Get ApiVersion

### Get information about all API versions supported by this Looker instance. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get ApiVersion
    api_response = api_instance.versions(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ApiVersion**](ApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whitelabel_configuration**
> WhitelabelConfiguration whitelabel_configuration(fields=fields)

Get Whitelabel configuration

### This feature is enabled only by special license. ### Gets the whitelabel configuration, which includes hiding documentation links, custom favicon uploading, etc. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ConfigApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Whitelabel configuration
    api_response = api_instance.whitelabel_configuration(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->whitelabel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**WhitelabelConfiguration**](WhitelabelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

