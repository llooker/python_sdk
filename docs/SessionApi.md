# swagger_client.SessionApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session**](SessionApi.md#session) | **GET** /session | Get Session
[**update_session**](SessionApi.md#update_session) | **PATCH** /session | Update Session


# **session**
> ApiSession session()

Get Session

### Get API Session  Returns information about the current API session, such as which workspace is selected for the session. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try: 
    # Get Session
    api_response = api_instance.session()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSession**](ApiSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_session**
> ApiSession update_session(body)

Update Session

### Update API Session  #### API Session Workspace  You can use this endpoint to change the active workspace for the current API session.  Only one workspace can be active in a session. The active workspace can be changed any number of times in a session.  The default workspace for API sessions is the \"production\" workspace.  All Looker APIs that use projects or lookml models (such as running queries) will use the version of project and model files defined by this workspace for the lifetime of the current API session or until the session workspace is changed again.  An API session has the same lifetime as the access_token used to authenticate API requests. Each successful API login generates a new access_token and a new API session.  If your Looker API client application needs to work in a dev workspace across multiple API sessions, be sure to select the dev workspace after each login. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
body = swagger_client.ApiSession() # ApiSession | Session

try: 
    # Update Session
    api_response = api_instance.update_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiSession**](ApiSession.md)| Session | 

### Return type

[**ApiSession**](ApiSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

