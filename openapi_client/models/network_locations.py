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


class NetworkLocations(object):
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
        'location': 'str'
    }

    attribute_map = {
        'id': 'id',
        'location': 'location'
    }

    def __init__(self, id=None, location=None, local_vars_configuration=None):  # noqa: E501
        """NetworkLocations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._location = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.location = location

    @property
    def id(self):
        """Gets the id of this NetworkLocations.  # noqa: E501


        :return: The id of this NetworkLocations.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkLocations.


        :param id: The id of this NetworkLocations.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this NetworkLocations.  # noqa: E501

        Location of network testing: Examples: VPN, Internet or Internal.  # noqa: E501

        :return: The location of this NetworkLocations.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this NetworkLocations.

        Location of network testing: Examples: VPN, Internet or Internal.  # noqa: E501

        :param location: The location of this NetworkLocations.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location is not None and len(location) > 500):
            raise ValueError("Invalid value for `location`, length must be less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location is not None and len(location) < 1):
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")  # noqa: E501

        self._location = location

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
        if not isinstance(other, NetworkLocations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkLocations):
            return True

        return self.to_dict() != other.to_dict()
