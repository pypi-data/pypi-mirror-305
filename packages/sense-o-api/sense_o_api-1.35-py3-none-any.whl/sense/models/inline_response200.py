# coding: utf-8

"""
    SENSE-O Northbound Intent API

    StackV SENSE-O Northbound REST API Documentation  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'list[Log]',
        'total_count': 'float',
        'timestamp': 'Object'
    }

    attribute_map = {
        'data': 'data',
        'total_count': 'totalCount',
        'timestamp': 'timestamp'
    }

    def __init__(self, data=None, total_count=None, timestamp=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._total_count = None
        self._timestamp = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if total_count is not None:
            self.total_count = total_count
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def data(self):
        """Gets the data of this InlineResponse200.  # noqa: E501

        Array of log entries.  # noqa: E501

        :return: The data of this InlineResponse200.  # noqa: E501
        :rtype: list[Log]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse200.

        Array of log entries.  # noqa: E501

        :param data: The data of this InlineResponse200.  # noqa: E501
        :type: list[Log]
        """

        self._data = data

    @property
    def total_count(self):
        """Gets the total_count of this InlineResponse200.  # noqa: E501

        Total amount of log entries available with specified filter.  # noqa: E501

        :return: The total_count of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this InlineResponse200.

        Total amount of log entries available with specified filter.  # noqa: E501

        :param total_count: The total_count of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._total_count = total_count

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse200.  # noqa: E501

        UNIX timestamp.  # noqa: E501

        :return: The timestamp of this InlineResponse200.  # noqa: E501
        :rtype: Object
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse200.

        UNIX timestamp.  # noqa: E501

        :param timestamp: The timestamp of this InlineResponse200.  # noqa: E501
        :type: Object
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
