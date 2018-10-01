# lookerapi.ApiAuthApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](ApiAuthApi.md#login) | **POST** /login | Login
[**login_user**](ApiAuthApi.md#login_user) | **POST** /login/{user_id} | Login user
[**logout**](ApiAuthApi.md#logout) | **DELETE** /logout | Logout


# **login**
> AccessToken login(client_id=client_id, client_secret=client_secret)

Login

### Present client credentials to obtain an authorization token  Looker API implements the OAuth2 [Resource Owner Password Credentials Grant](https://looker.com/docs/r/api/outh2_resource_owner_pc) pattern. The client credentials required for this login must be obtained by creating an API3 key on a user account in the Looker Admin console. The API3 key consists of a public `client_id` and a private `client_secret`.  The access token returned by `login` must be used in the HTTP Authorization header of subsequent API requests, like this: ``` Authorization: token 4QDkCyCtZzYgj4C2p2cj3csJH7zqS5RzKs2kTnG4 ``` Replace \"4QDkCy...\" with the `access_token` value returned by `login`. The word 'token' is a string literal and must be included exactly as shown.  For more information and detailed examples of Looker API authorization, see [How to Authenticate to Looker API3](https://github.com/looker/looker-sdk-ruby/blob/master/authentication.md). 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ApiAuthApi()
client_id = 'client_id_example' # str | client_id part of API3 Key. (optional)
client_secret = 'client_secret_example' # str | client_secret part of API3 Key. (optional)

try: 
    # Login
    api_response = api_instance.login(client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client_id part of API3 Key. | [optional] 
 **client_secret** | **str**| client_secret part of API3 Key. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user**
> AccessToken login_user(user_id)

Login user

### Create an access token for a given user.  This can only be called by an authenticated admin user. It allows that admin to generate a new authentication token for the user with the given user id. That token can then be used for subsequent API calls - which are then performed *as* that target user.  The target user does *not* need to have a pre-existing API client_id/client_secret pair. And, no such credentials are created by this call.  This allows for building systems where api user authentication for an arbitrary number of users is done outside of Looker and funneled through a single 'service account' with admin permissions. Note that a new access token is generated on each call. If target users are going to be making numerous API calls in a short period then it is wise to cache this authentication token rather than call this before each of those API calls.  See 'login' for more detail on the access token and how to use it. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ApiAuthApi()
user_id = 789 # int | Id of user.

try: 
    # Login user
    api_response = api_instance.login_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> str logout()

Logout

### Logout of the API and invalidate the current access token. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.ApiAuthApi()

try: 
    # Logout
    api_response = api_instance.logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiAuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

