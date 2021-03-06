# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SonarqubeIssue(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'key': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, id=None, key=None, status=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SonarqubeIssue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._key = None
        self._status = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.key = key
        self.status = status
        self.type = type

    @property
    def id(self):
        """Gets the id of this SonarqubeIssue.  # noqa: E501


        :return: The id of this SonarqubeIssue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SonarqubeIssue.


        :param id: The id of this SonarqubeIssue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this SonarqubeIssue.  # noqa: E501

        SonarQube issue key  # noqa: E501

        :return: The key of this SonarqubeIssue.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SonarqubeIssue.

        SonarQube issue key  # noqa: E501

        :param key: The key of this SonarqubeIssue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) > 30):
            raise ValueError("Invalid value for `key`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def status(self):
        """Gets the status of this SonarqubeIssue.  # noqa: E501

        SonarQube issue status  # noqa: E501

        :return: The status of this SonarqubeIssue.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SonarqubeIssue.

        SonarQube issue status  # noqa: E501

        :param status: The status of this SonarqubeIssue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) > 20):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this SonarqubeIssue.  # noqa: E501

        SonarQube issue type  # noqa: E501

        :return: The type of this SonarqubeIssue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SonarqubeIssue.

        SonarQube issue type  # noqa: E501

        :param type: The type of this SonarqubeIssue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 20):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SonarqubeIssue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SonarqubeIssue):
            return True

        return self.to_dict() != other.to_dict()
