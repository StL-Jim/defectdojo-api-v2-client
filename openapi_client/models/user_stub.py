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


class UserStub(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, local_vars_configuration=None):  # noqa: E501
        """UserStub - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def id(self):
        """Gets the id of this UserStub.  # noqa: E501


        :return: The id of this UserStub.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserStub.


        :param id: The id of this UserStub.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserStub.  # noqa: E501

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :return: The username of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserStub.

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :param username: The username of this UserStub.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 150):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `150`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and not re.search(r'^[\w.@+-]+$', username)):  # noqa: E501
            raise ValueError(r"Invalid value for `username`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this UserStub.  # noqa: E501


        :return: The first_name of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserStub.


        :param first_name: The first_name of this UserStub.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 150):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `150`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserStub.  # noqa: E501


        :return: The last_name of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserStub.


        :param last_name: The last_name of this UserStub.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 150):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `150`")  # noqa: E501

        self._last_name = last_name

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
        if not isinstance(other, UserStub):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserStub):
            return True

        return self.to_dict() != other.to_dict()