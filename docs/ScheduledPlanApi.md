# swagger_client.ScheduledPlanApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_scheduled_plans**](ScheduledPlanApi.md#all_scheduled_plans) | **GET** /scheduled_plans | Get All Scheduled Plans
[**create_scheduled_plan**](ScheduledPlanApi.md#create_scheduled_plan) | **POST** /scheduled_plans | Create Scheduled Plan
[**delete_scheduled_plan**](ScheduledPlanApi.md#delete_scheduled_plan) | **DELETE** /scheduled_plans/{scheduled_plan_id} | Delete Scheduled Plan
[**scheduled_plan**](ScheduledPlanApi.md#scheduled_plan) | **GET** /scheduled_plans/{scheduled_plan_id} | Get Scheduled Plan
[**scheduled_plan_run_once**](ScheduledPlanApi.md#scheduled_plan_run_once) | **POST** /scheduled_plans/run_once | Run Scheduled Plan Once
[**scheduled_plans_for_dashboard**](ScheduledPlanApi.md#scheduled_plans_for_dashboard) | **GET** /scheduled_plans/dashboard/{dashboard_id} | Scheduled Plans for Dashboard
[**scheduled_plans_for_look**](ScheduledPlanApi.md#scheduled_plans_for_look) | **GET** /scheduled_plans/look/{look_id} | Scheduled Plans for Look
[**scheduled_plans_for_lookml_dashboard**](ScheduledPlanApi.md#scheduled_plans_for_lookml_dashboard) | **GET** /scheduled_plans/lookml_dashboard/{lookml_dashboard_id} | Scheduled Plans for LookML Dashboard
[**scheduled_plans_for_space**](ScheduledPlanApi.md#scheduled_plans_for_space) | **GET** /scheduled_plans/space/{space_id} | Scheduled Plans for Space
[**update_scheduled_plan**](ScheduledPlanApi.md#update_scheduled_plan) | **PATCH** /scheduled_plans/{scheduled_plan_id} | Update Scheduled Plan


# **all_scheduled_plans**
> list[ScheduledPlan] all_scheduled_plans(user_id=user_id, fields=fields)

Get All Scheduled Plans

### Get All Scheduled Plans  Returns all scheduled plans owned by the caller or given user.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   The caller must have `see_schedules` permission to see other users' scheduled plans.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get All Scheduled Plans
    api_response = api_instance.all_scheduled_plans(user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->all_scheduled_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scheduled_plan**
> ScheduledPlan create_scheduled_plan(body=body)

Create Scheduled Plan

### Create a Scheduled Plan  Create a scheduled plan to render a Look or Dashboard on a recurring schedule.  The queries that provide the data for the look or dashboard are run in the context of user account that owns the scheduled plan.  Admins can create scheduled plans on behalf of other users by specifying a user id.  Scheduled plan destinations must specify the data format to produce and send to the destination  Scheduled Plan Destination formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
body = swagger_client.ScheduledPlan() # ScheduledPlan | Scheduled Plan (optional)

try: 
    # Create Scheduled Plan
    api_response = api_instance.create_scheduled_plan(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->create_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_plan**
> str delete_scheduled_plan(scheduled_plan_id)

Delete Scheduled Plan

### Delete a Scheduled Plan  Normal users can only delete their own scheduled plans. Admins can delete other users' scheduled plans. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id

try: 
    # Delete Scheduled Plan
    api_response = api_instance.delete_scheduled_plan(scheduled_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->delete_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan**
> ScheduledPlan scheduled_plan(scheduled_plan_id, fields=fields)

Get Scheduled Plan

### Get Information About a Scheduled Plan  Admins can fetch information about other users' Scheduled Plans. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Scheduled Plan
    api_response = api_instance.scheduled_plan(scheduled_plan_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan_run_once**
> ScheduledPlan scheduled_plan_run_once(body=body)

Run Scheduled Plan Once

### Run a Scheduled Plan Immediately  Create a scheduled plan that runs only once, and immediately.  This can be useful for testing a Scheduled Plan before committing to a production schedule.  Admins can create scheduled plans on behalf of other users by specifying a user id.  Scheduled plan destinations must specify the data format to produce and send to the destination  Scheduled Plan Destination formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
body = swagger_client.ScheduledPlan() # ScheduledPlan | Scheduled Plan (optional)

try: 
    # Run Scheduled Plan Once
    api_response = api_instance.scheduled_plan_run_once(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plan_run_once: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_dashboard**
> list[ScheduledPlan] scheduled_plans_for_dashboard(dashboard_id, user_id=user_id, fields=fields)

Scheduled Plans for Dashboard

### Get Scheduled Plans for a Dashboard  Returns all scheduled plans owned by the caller or given user, for a given dashboard.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   The caller must have `see_schedules` permission to see other users' scheduled plans.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
dashboard_id = 789 # int | Dashboard Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Scheduled Plans for Dashboard
    api_response = api_instance.scheduled_plans_for_dashboard(dashboard_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| Dashboard Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_look**
> list[ScheduledPlan] scheduled_plans_for_look(look_id, user_id=user_id, fields=fields)

Scheduled Plans for Look

### Get Scheduled Plans for a Look  Returns all scheduled plans owned by the caller or given user, for a given look.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   The caller must have `see_schedules` permission to see other users' scheduled plans.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
look_id = 789 # int | Look Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Scheduled Plans for Look
    api_response = api_instance.scheduled_plans_for_look(look_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_look: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Look Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_lookml_dashboard**
> list[ScheduledPlan] scheduled_plans_for_lookml_dashboard(lookml_dashboard_id, user_id=user_id, fields=fields)

Scheduled Plans for LookML Dashboard

### Get Scheduled Plans for a LookML Dashboard  Returns all scheduled plans owned by the caller or given user, for a given LookML dashboard.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   The caller must have `see_schedules` permission to see other users' scheduled plans.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
lookml_dashboard_id = 789 # int | LookML Dashboard Id
user_id = 789 # int | User Id (default is requesting user if not specified) (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Scheduled Plans for LookML Dashboard
    api_response = api_instance.scheduled_plans_for_lookml_dashboard(lookml_dashboard_id, user_id=user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_lookml_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_dashboard_id** | **int**| LookML Dashboard Id | 
 **user_id** | **int**| User Id (default is requesting user if not specified) | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_for_space**
> list[ScheduledPlan] scheduled_plans_for_space(space_id, fields=fields)

Scheduled Plans for Space

### Get Scheduled Plans for a Space  Returns scheduled plans owned by the caller for a given space id. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
space_id = 789 # int | Space Id
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Scheduled Plans for Space
    api_response = api_instance.scheduled_plans_for_space(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->scheduled_plans_for_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **int**| Space Id | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_plan**
> ScheduledPlan update_scheduled_plan(scheduled_plan_id, body)

Update Scheduled Plan

### Update a Scheduled Plan  Admins can update other users' Scheduled Plans.  Note: Any scheduled plan destinations specified in an update will **replace** all scheduled plan destinations currently defined for the scheduled plan.  For Example: If a scheduled plan has destinations A, B, and C, and you call update on this scheduled plan specifying only B in the destinations, then destinations A and C will be deleted by the update.  Scheduled plan destinations must specify the data format to produce and send to the destination  Scheduled Plan Destination formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.   

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id
body = swagger_client.ScheduledPlan() # ScheduledPlan | Scheduled Plan

try: 
    # Update Scheduled Plan
    api_response = api_instance.update_scheduled_plan(scheduled_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanApi->update_scheduled_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| Scheduled Plan | 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

