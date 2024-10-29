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

class ConnectionSuggestIpRange(object):
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
        'name': 'str',
        'start': 'str',
        'end': 'str'
    }

    attribute_map = {
        'name': 'name',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, name=None, start=None, end=None):  # noqa: E501
        """ConnectionSuggestIpRange - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._start = None
        self._end = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def name(self):
        """Gets the name of this ConnectionSuggestIpRange.  # noqa: E501


        :return: The name of this ConnectionSuggestIpRange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionSuggestIpRange.


        :param name: The name of this ConnectionSuggestIpRange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start(self):
        """Gets the start of this ConnectionSuggestIpRange.  # noqa: E501

        Start of the IP range suggestion.  # noqa: E501

        :return: The start of this ConnectionSuggestIpRange.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ConnectionSuggestIpRange.

        Start of the IP range suggestion.  # noqa: E501

        :param start: The start of this ConnectionSuggestIpRange.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this ConnectionSuggestIpRange.  # noqa: E501

        End of the IP range suggestion.  # noqa: E501

        :return: The end of this ConnectionSuggestIpRange.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ConnectionSuggestIpRange.

        End of the IP range suggestion.  # noqa: E501

        :param end: The end of this ConnectionSuggestIpRange.  # noqa: E501
        :type: str
        """

        self._end = end

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
        if issubclass(ConnectionSuggestIpRange, dict):
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
        if not isinstance(other, ConnectionSuggestIpRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
