# swagger_client.WorkspaceApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_workspaces**](WorkspaceApi.md#all_workspaces) | **GET** /workspaces | Get All Workspaces
[**workspace**](WorkspaceApi.md#workspace) | **GET** /workspaces/{workspace_id} | Get Workspace


# **all_workspaces**
> list[Workspace] all_workspaces()

Get All Workspaces

### Get All Workspaces  Returns all workspaces available to the calling user. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspaceApi()

try: 
    # Get All Workspaces
    api_response = api_instance.all_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceApi->all_workspaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Workspace]**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace**
> Workspace workspace(workspace_id)

Get Workspace

### Get A Workspace  Returns information about a workspace such as the git status and selected branches of all projects available to the caller's user account.  A workspace defines which versions of project files will be used to evaluate expressions and operations that use model definitions - operations such as running queries or rendering dashboards. Each project has its own git repository, and each project in a workspace may be configured to reference particular branch or revision within their respective repositories.  There are two predefined workspaces available: \"production\" and \"dev\".  The production workspace is shared across all Looker users. Models in the production workspace are read-only. Changing files in production is accomplished by modifying files in a git branch and using Pull Requests to merge the changes from the dev branch into the production branch, and then telling Looker to sync with production.  The dev workspace is local to each Looker user. Changes made to project/model files in the dev workspace only affect that user, and only when the dev workspace is selected as the active workspace for the API session. (See set_session_workspace()).  The dev workspace is NOT unique to an API session. Two applications accessing the Looker API using the same user account will see the same files in the dev workspace. To avoid collisions between API clients it's best to have each client login with API3 credentials for a different user account.  Changes made to files in a dev workspace are persistent across API sessions. It's a good idea to commit any changes you've made to the git repository, but not strictly required. Your modified files reside in a special user-specific directory on the Looker server and will still be there when you login in again later and use update_session(workspace_id: \"dev\") to select the dev workspace for the new API session. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspaceApi()
workspace_id = 'workspace_id_example' # str | Id of the workspace 

try: 
    # Get Workspace
    api_response = api_instance.workspace(workspace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceApi->workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Id of the workspace  | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

