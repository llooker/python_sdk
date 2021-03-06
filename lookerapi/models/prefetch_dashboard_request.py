# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrefetchDashboardRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ttl=None, access_filters=None, dashboard_filters=None, created_at=None, computation_time=None, result_size_bytes=None, hit_count=None, touched_at=None, can=None):
        """
        PrefetchDashboardRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ttl': 'int',
            'access_filters': 'list[PrefetchAccessFilterValue]',
            'dashboard_filters': 'list[PrefetchDashboardFilterValue]',
            'created_at': 'datetime',
            'computation_time': 'float',
            'result_size_bytes': 'int',
            'hit_count': 'int',
            'touched_at': 'datetime',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'ttl': 'ttl',
            'access_filters': 'access_filters',
            'dashboard_filters': 'dashboard_filters',
            'created_at': 'created_at',
            'computation_time': 'computation_time',
            'result_size_bytes': 'result_size_bytes',
            'hit_count': 'hit_count',
            'touched_at': 'touched_at',
            'can': 'can'
        }

        self._ttl = ttl
        self._access_filters = access_filters
        self._dashboard_filters = dashboard_filters
        self._created_at = created_at
        self._computation_time = computation_time
        self._result_size_bytes = result_size_bytes
        self._hit_count = hit_count
        self._touched_at = touched_at
        self._can = can

    @property
    def ttl(self):
        """
        Gets the ttl of this PrefetchDashboardRequest.
        Number of seconds prefetch will live for.

        :return: The ttl of this PrefetchDashboardRequest.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this PrefetchDashboardRequest.
        Number of seconds prefetch will live for.

        :param ttl: The ttl of this PrefetchDashboardRequest.
        :type: int
        """

        self._ttl = ttl

    @property
    def access_filters(self):
        """
        Gets the access_filters of this PrefetchDashboardRequest.
        Access filters to apply when running queries for prefetch.

        :return: The access_filters of this PrefetchDashboardRequest.
        :rtype: list[PrefetchAccessFilterValue]
        """
        return self._access_filters

    @access_filters.setter
    def access_filters(self, access_filters):
        """
        Sets the access_filters of this PrefetchDashboardRequest.
        Access filters to apply when running queries for prefetch.

        :param access_filters: The access_filters of this PrefetchDashboardRequest.
        :type: list[PrefetchAccessFilterValue]
        """

        self._access_filters = access_filters

    @property
    def dashboard_filters(self):
        """
        Gets the dashboard_filters of this PrefetchDashboardRequest.
        Dashboard filters to apply when running queries for prefetch.

        :return: The dashboard_filters of this PrefetchDashboardRequest.
        :rtype: list[PrefetchDashboardFilterValue]
        """
        return self._dashboard_filters

    @dashboard_filters.setter
    def dashboard_filters(self, dashboard_filters):
        """
        Sets the dashboard_filters of this PrefetchDashboardRequest.
        Dashboard filters to apply when running queries for prefetch.

        :param dashboard_filters: The dashboard_filters of this PrefetchDashboardRequest.
        :type: list[PrefetchDashboardFilterValue]
        """

        self._dashboard_filters = dashboard_filters

    @property
    def created_at(self):
        """
        Gets the created_at of this PrefetchDashboardRequest.
        Time when prefetch was created.

        :return: The created_at of this PrefetchDashboardRequest.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this PrefetchDashboardRequest.
        Time when prefetch was created.

        :param created_at: The created_at of this PrefetchDashboardRequest.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def computation_time(self):
        """
        Gets the computation_time of this PrefetchDashboardRequest.
        Number of seconds it took to compute results for prefetch.

        :return: The computation_time of this PrefetchDashboardRequest.
        :rtype: float
        """
        return self._computation_time

    @computation_time.setter
    def computation_time(self, computation_time):
        """
        Sets the computation_time of this PrefetchDashboardRequest.
        Number of seconds it took to compute results for prefetch.

        :param computation_time: The computation_time of this PrefetchDashboardRequest.
        :type: float
        """

        self._computation_time = computation_time

    @property
    def result_size_bytes(self):
        """
        Gets the result_size_bytes of this PrefetchDashboardRequest.
        Size of result.

        :return: The result_size_bytes of this PrefetchDashboardRequest.
        :rtype: int
        """
        return self._result_size_bytes

    @result_size_bytes.setter
    def result_size_bytes(self, result_size_bytes):
        """
        Sets the result_size_bytes of this PrefetchDashboardRequest.
        Size of result.

        :param result_size_bytes: The result_size_bytes of this PrefetchDashboardRequest.
        :type: int
        """

        self._result_size_bytes = result_size_bytes

    @property
    def hit_count(self):
        """
        Gets the hit_count of this PrefetchDashboardRequest.
        Number of times prefetch has been accessed.

        :return: The hit_count of this PrefetchDashboardRequest.
        :rtype: int
        """
        return self._hit_count

    @hit_count.setter
    def hit_count(self, hit_count):
        """
        Sets the hit_count of this PrefetchDashboardRequest.
        Number of times prefetch has been accessed.

        :param hit_count: The hit_count of this PrefetchDashboardRequest.
        :type: int
        """

        self._hit_count = hit_count

    @property
    def touched_at(self):
        """
        Gets the touched_at of this PrefetchDashboardRequest.
        Time when prefetch was last accessed.

        :return: The touched_at of this PrefetchDashboardRequest.
        :rtype: datetime
        """
        return self._touched_at

    @touched_at.setter
    def touched_at(self, touched_at):
        """
        Sets the touched_at of this PrefetchDashboardRequest.
        Time when prefetch was last accessed.

        :param touched_at: The touched_at of this PrefetchDashboardRequest.
        :type: datetime
        """

        self._touched_at = touched_at

    @property
    def can(self):
        """
        Gets the can of this PrefetchDashboardRequest.
        Operations the current user is able to perform on this object

        :return: The can of this PrefetchDashboardRequest.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this PrefetchDashboardRequest.
        Operations the current user is able to perform on this object

        :param can: The can of this PrefetchDashboardRequest.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PrefetchDashboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
