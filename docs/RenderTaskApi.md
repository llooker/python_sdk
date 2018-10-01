# swagger_client.RenderTaskApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_render_task**](RenderTaskApi.md#create_dashboard_render_task) | **POST** /render_tasks/dashboards/{dashboard_id}/{result_format} | Create Dashboard Render Task
[**create_look_render_task**](RenderTaskApi.md#create_look_render_task) | **POST** /render_tasks/looks/{look_id}/{result_format} | Create Look Render Task
[**create_lookml_dashboard_render_task**](RenderTaskApi.md#create_lookml_dashboard_render_task) | **POST** /render_tasks/lookml_dashboards/{dashboard_id}/{result_format} | Create Lookml Dashboard Render Task
[**create_query_render_task**](RenderTaskApi.md#create_query_render_task) | **POST** /render_tasks/queries/{query_id}/{result_format} | Create Query Render Task
[**render_task**](RenderTaskApi.md#render_task) | **GET** /render_tasks/{render_task_id} | Get Render Task
[**render_task_results**](RenderTaskApi.md#render_task_results) | **GET** /render_tasks/{render_task_id}/results | Render Task Results


# **create_dashboard_render_task**
> RenderTask create_dashboard_render_task(dashboard_id, result_format, body, width, height, fields=fields)

Create Dashboard Render Task

### Create a new task to render a dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
dashboard_id = 789 # int | Id of dashboard to render
result_format = 'result_format_example' # str | Output type: pdf, png, or jpg
body = swagger_client.CreateDashboardRenderTask() # CreateDashboardRenderTask | Dashboard render task parameters
width = 789 # int | Output width in pixels
height = 789 # int | Output height in pixels
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Dashboard Render Task
    api_response = api_instance.create_dashboard_render_task(dashboard_id, result_format, body, width, height, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->create_dashboard_render_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| Id of dashboard to render | 
 **result_format** | **str**| Output type: pdf, png, or jpg | 
 **body** | [**CreateDashboardRenderTask**](CreateDashboardRenderTask.md)| Dashboard render task parameters | 
 **width** | **int**| Output width in pixels | 
 **height** | **int**| Output height in pixels | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RenderTask**](RenderTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_look_render_task**
> RenderTask create_look_render_task(look_id, result_format, width, height, fields=fields)

Create Look Render Task

### Create a new task to render a look to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
look_id = 789 # int | Id of look to render
result_format = 'result_format_example' # str | Output type: png, or jpg
width = 789 # int | Output width in pixels
height = 789 # int | Output height in pixels
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Look Render Task
    api_response = api_instance.create_look_render_task(look_id, result_format, width, height, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->create_look_render_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look to render | 
 **result_format** | **str**| Output type: png, or jpg | 
 **width** | **int**| Output width in pixels | 
 **height** | **int**| Output height in pixels | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RenderTask**](RenderTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lookml_dashboard_render_task**
> RenderTask create_lookml_dashboard_render_task(dashboard_id, result_format, body, width, height, fields=fields)

Create Lookml Dashboard Render Task

### Create a new task to render a lookml dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
dashboard_id = 'dashboard_id_example' # str | Id of lookml dashboard to render
result_format = 'result_format_example' # str | Output type: pdf, png, or jpg
body = swagger_client.CreateDashboardRenderTask() # CreateDashboardRenderTask | Dashboard render task parameters
width = 789 # int | Output width in pixels
height = 789 # int | Output height in pixels
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Lookml Dashboard Render Task
    api_response = api_instance.create_lookml_dashboard_render_task(dashboard_id, result_format, body, width, height, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->create_lookml_dashboard_render_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of lookml dashboard to render | 
 **result_format** | **str**| Output type: pdf, png, or jpg | 
 **body** | [**CreateDashboardRenderTask**](CreateDashboardRenderTask.md)| Dashboard render task parameters | 
 **width** | **int**| Output width in pixels | 
 **height** | **int**| Output height in pixels | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RenderTask**](RenderTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_query_render_task**
> RenderTask create_query_render_task(query_id, result_format, width, height, fields=fields)

Create Query Render Task

### Create a new task to render an existing query to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
query_id = 789 # int | Id of the query to render
result_format = 'result_format_example' # str | Output type: png or jpg
width = 789 # int | Output width in pixels
height = 789 # int | Output height in pixels
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Create Query Render Task
    api_response = api_instance.create_query_render_task(query_id, result_format, width, height, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->create_query_render_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **int**| Id of the query to render | 
 **result_format** | **str**| Output type: png or jpg | 
 **width** | **int**| Output width in pixels | 
 **height** | **int**| Output height in pixels | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RenderTask**](RenderTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_task**
> RenderTask render_task(render_task_id, fields=fields)

Get Render Task

### Get information about a render task.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
render_task_id = 'render_task_id_example' # str | Id of render task
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get Render Task
    api_response = api_instance.render_task(render_task_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->render_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_task_id** | **str**| Id of render task | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RenderTask**](RenderTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_task_results**
> str render_task_results(render_task_id)

Render Task Results

### Get the document or image produced by a completed render task.  Returns `102 Processing` if the render task has not completed. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenderTaskApi()
render_task_id = 'render_task_id_example' # str | Id of render task

try: 
    # Render Task Results
    api_response = api_instance.render_task_results(render_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenderTaskApi->render_task_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_task_id** | **str**| Id of render task | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

