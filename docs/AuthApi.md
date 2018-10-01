# lookerapi.AuthApi

All URIs are relative to *https://demo.looker.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_oidc_test_config**](AuthApi.md#create_oidc_test_config) | **POST** /oidc_test_configs | Create OIDC Test Configuration
[**create_saml_test_config**](AuthApi.md#create_saml_test_config) | **POST** /saml_test_configs | Create SAML Test Configuration
[**delete_oidc_test_config**](AuthApi.md#delete_oidc_test_config) | **DELETE** /oidc_test_configs/{test_slug} | Delete OIDC Test Configuration
[**delete_saml_test_config**](AuthApi.md#delete_saml_test_config) | **DELETE** /saml_test_configs/{test_slug} | Delete SAML Test Configuration
[**fetch_and_parse_saml_idp_metadata**](AuthApi.md#fetch_and_parse_saml_idp_metadata) | **POST** /fetch_and_parse_saml_idp_metadata | Parse SAML IdP Url
[**ldap_config**](AuthApi.md#ldap_config) | **GET** /ldap_config | Get LDAP Configuration
[**oidc_config**](AuthApi.md#oidc_config) | **GET** /oidc_config | Get OIDC Configuration
[**oidc_test_config**](AuthApi.md#oidc_test_config) | **GET** /oidc_test_configs/{test_slug} | Get OIDC Test Configuration
[**parse_saml_idp_metadata**](AuthApi.md#parse_saml_idp_metadata) | **POST** /parse_saml_idp_metadata | Parse SAML IdP XML
[**saml_config**](AuthApi.md#saml_config) | **GET** /saml_config | Get SAML Configuration
[**saml_test_config**](AuthApi.md#saml_test_config) | **GET** /saml_test_configs/{test_slug} | Get SAML Test Configuration
[**test_ldap_config_auth**](AuthApi.md#test_ldap_config_auth) | **PUT** /ldap_config/test_auth | Test LDAP Auth
[**test_ldap_config_connection**](AuthApi.md#test_ldap_config_connection) | **PUT** /ldap_config/test_connection | Test LDAP Connection
[**test_ldap_config_user_auth**](AuthApi.md#test_ldap_config_user_auth) | **PUT** /ldap_config/test_user_auth | Test LDAP User Auth
[**test_ldap_config_user_info**](AuthApi.md#test_ldap_config_user_info) | **PUT** /ldap_config/test_user_info | Test LDAP User Info
[**update_ldap_config**](AuthApi.md#update_ldap_config) | **PATCH** /ldap_config | Update LDAP Configuration
[**update_oidc_config**](AuthApi.md#update_oidc_config) | **PATCH** /oidc_config | Update OIDC Configuration
[**update_saml_config**](AuthApi.md#update_saml_config) | **PATCH** /saml_config | Update SAML Configuration


# **create_oidc_test_config**
> OIDCConfig create_oidc_test_config(body)

Create OIDC Test Configuration

### Create a OIDC test configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.OIDCConfig() # OIDCConfig | OIDC test config

try: 
    # Create OIDC Test Configuration
    api_response = api_instance.create_oidc_test_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_oidc_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OIDCConfig**](OIDCConfig.md)| OIDC test config | 

### Return type

[**OIDCConfig**](OIDCConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saml_test_config**
> SamlConfig create_saml_test_config(body)

Create SAML Test Configuration

### Create a SAML test configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.SamlConfig() # SamlConfig | SAML test config

try: 
    # Create SAML Test Configuration
    api_response = api_instance.create_saml_test_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_saml_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConfig**](SamlConfig.md)| SAML test config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oidc_test_config**
> str delete_oidc_test_config(test_slug)

Delete OIDC Test Configuration

### Delete a OIDC test configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # Delete OIDC Test Configuration
    api_response = api_instance.delete_oidc_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->delete_oidc_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_test_config**
> str delete_saml_test_config(test_slug)

Delete SAML Test Configuration

### Delete a SAML test configuration. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # Delete SAML Test Configuration
    api_response = api_instance.delete_saml_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->delete_saml_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_and_parse_saml_idp_metadata**
> SamlMetadataParseResult fetch_and_parse_saml_idp_metadata(body)

Parse SAML IdP Url

### Fetch the given url and parse it as a SAML IdP metadata document and return the result. Note that this requires that the url be public or at least at a location where the Looker instance can fetch it without requiring any special authentication. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = 'body_example' # str | SAML IdP metadata public url

try: 
    # Parse SAML IdP Url
    api_response = api_instance.fetch_and_parse_saml_idp_metadata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->fetch_and_parse_saml_idp_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SAML IdP metadata public url | 

### Return type

[**SamlMetadataParseResult**](SamlMetadataParseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_config**
> LDAPConfig ldap_config()

Get LDAP Configuration

### Get the LDAP configuration.  Looker can be optionally configured to authenticate users against an Active Directory or other LDAP directory server. LDAP setup requires coordination with an administrator of that directory server.  Only Looker administrators can read and update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single LDAP configuration. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  LDAP is enabled or disabled for Looker using the **enabled** field.  Looker will never return an **auth_password** field. That value can be set, but never retrieved.  See the [Looker LDAP docs](https://www.looker.com/docs/r/api/ldap_setup) for additional information. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()

try: 
    # Get LDAP Configuration
    api_response = api_instance.ldap_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->ldap_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LDAPConfig**](LDAPConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_config**
> OIDCConfig oidc_config()

Get OIDC Configuration

### Get the OIDC configuration.  Looker can be optionally configured to authenticate users against an OpenID Connect (OIDC) authentication server. OIDC setup requires coordination with an administrator of that server.  Only Looker administrators can read and update the OIDC configuration.  Configuring OIDC impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single OIDC configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  OIDC is enabled or disabled for Looker using the **enabled** field. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()

try: 
    # Get OIDC Configuration
    api_response = api_instance.oidc_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oidc_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OIDCConfig**](OIDCConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_test_config**
> OIDCConfig oidc_test_config(test_slug)

Get OIDC Test Configuration

### Get a OIDC test configuration by test_slug. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # Get OIDC Test Configuration
    api_response = api_instance.oidc_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oidc_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

[**OIDCConfig**](OIDCConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_saml_idp_metadata**
> SamlMetadataParseResult parse_saml_idp_metadata(body)

Parse SAML IdP XML

### Parse the given xml as a SAML IdP metadata document and return the result. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = 'body_example' # str | SAML IdP metadata xml

try: 
    # Parse SAML IdP XML
    api_response = api_instance.parse_saml_idp_metadata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->parse_saml_idp_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SAML IdP metadata xml | 

### Return type

[**SamlMetadataParseResult**](SamlMetadataParseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_config**
> SamlConfig saml_config()

Get SAML Configuration

### Get the SAML configuration.  Looker can be optionally configured to authenticate users against a SAML authentication server. SAML setup requires coordination with an administrator of that server.  Only Looker administrators can read and update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single SAML configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  SAML is enabled or disabled for Looker using the **enabled** field. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()

try: 
    # Get SAML Configuration
    api_response = api_instance.saml_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->saml_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_test_config**
> SamlConfig saml_test_config(test_slug)

Get SAML Test Configuration

### Get a SAML test configuration by test_slug. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # Get SAML Test Configuration
    api_response = api_instance.saml_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->saml_test_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_auth**
> LDAPConfigTestResult test_ldap_config_auth(body)

Test LDAP Auth

### Test the connection authentication settings for an LDAP configuration.  This tests that the connection is possible and that a 'server' account to be used by Looker can       authenticate to the LDAP server given connection and authentication information.  **connection_host**, **connection_port**, and **auth_username**, are required.       **connection_tls** and **auth_password** are optional.  Example: ```json {   \"connection_host\": \"ldap.example.com\",   \"connection_port\": \"636\",   \"connection_tls\": true,   \"auth_username\": \"cn=looker,dc=example,dc=com\",   \"auth_password\": \"secret\" } ```  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  The active LDAP settings are not modified.  

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # Test LDAP Auth
    api_response = api_instance.test_ldap_config_auth(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->test_ldap_config_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_connection**
> LDAPConfigTestResult test_ldap_config_connection(body)

Test LDAP Connection

### Test the connection settings for an LDAP configuration.  This tests that the connection is possible given a connection_host and connection_port.  **connection_host** and **connection_port** are required. **connection_tls** is optional.  Example: ```json {   \"connection_host\": \"ldap.example.com\",   \"connection_port\": \"636\",   \"connection_tls\": true } ```  No authentication to the LDAP server is attempted.  The active LDAP settings are not modified. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # Test LDAP Connection
    api_response = api_instance.test_ldap_config_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->test_ldap_config_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_user_auth**
> LDAPConfigTestResult test_ldap_config_user_auth(body)

Test LDAP User Auth

### Test the user authentication settings for an LDAP configuration.  This test accepts a full LDAP configuration along with a username/password pair and attempts to       authenticate the user with the LDAP server. The configuration is validated before attempting the       authentication.  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  **test_ldap_user** and **test_ldap_password** are required.  The active LDAP settings are not modified.  

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # Test LDAP User Auth
    api_response = api_instance.test_ldap_config_user_auth(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->test_ldap_config_user_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_user_info**
> LDAPConfigTestResult test_ldap_config_user_info(body)

Test LDAP User Info

### Test the user authentication settings for an LDAP configuration without authenticating the user.  This test will let you easily test the mapping for user properties and roles for any user without      needing to authenticate as that user.  This test accepts a full LDAP configuration along with a username and attempts to find the full info      for the user from the LDAP server without actually authenticating the user. So, user password is not      required.The configuration is validated before attempting to contact the server.  **test_ldap_user** is required.  The active LDAP settings are not modified.  

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # Test LDAP User Info
    api_response = api_instance.test_ldap_config_user_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->test_ldap_config_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_config**
> LDAPConfig update_ldap_config(body)

Update LDAP Configuration

### Update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the LDAP configuration.  LDAP is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any LDAP setting changes be tested using the APIs below before being set globally.  See the [Looker LDAP docs](https://www.looker.com/docs/r/api/ldap_setup) for additional information. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # Update LDAP Configuration
    api_response = api_instance.update_ldap_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->update_ldap_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfig**](LDAPConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oidc_config**
> OIDCConfig update_oidc_config(body)

Update OIDC Configuration

### Update the OIDC configuration.  Configuring OIDC impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the OIDC configuration.  OIDC is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any OIDC setting changes be tested using the APIs below before being set globally. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.OIDCConfig() # OIDCConfig | OIDC Config

try: 
    # Update OIDC Configuration
    api_response = api_instance.update_oidc_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->update_oidc_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OIDCConfig**](OIDCConfig.md)| OIDC Config | 

### Return type

[**OIDCConfig**](OIDCConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_config**
> SamlConfig update_saml_config(body)

Update SAML Configuration

### Update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the SAML configuration.  SAML is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any SAML setting changes be tested using the APIs below before being set globally. 

### Example 
```python
from __future__ import print_statement
import time
import lookerapi
from lookerapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerapi.AuthApi()
body = lookerapi.SamlConfig() # SamlConfig | SAML Config

try: 
    # Update SAML Configuration
    api_response = api_instance.update_saml_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->update_saml_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConfig**](SamlConfig.md)| SAML Config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

