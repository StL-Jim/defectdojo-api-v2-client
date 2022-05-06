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


class InlineResponse20030Prefetch(object):
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
        'product': 'dict(str, Product)',
        'role': 'dict(str, Role)',
        'user': 'dict(str, UserStub)'
    }

    attribute_map = {
        'product': 'product',
        'role': 'role',
        'user': 'user'
    }

    def __init__(self, product=None, role=None, user=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20030Prefetch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product = None
        self._role = None
        self._user = None
        self.discriminator = None

        if product is not None:
            self.product = product
        if role is not None:
            self.role = role
        if user is not None:
            self.user = user

    @property
    def product(self):
        """Gets the product of this InlineResponse20030Prefetch.  # noqa: E501


        :return: The product of this InlineResponse20030Prefetch.  # noqa: E501
        :rtype: dict(str, Product)
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InlineResponse20030Prefetch.


        :param product: The product of this InlineResponse20030Prefetch.  # noqa: E501
        :type: dict(str, Product)
        """

        self._product = product

    @property
    def role(self):
        """Gets the role of this InlineResponse20030Prefetch.  # noqa: E501


        :return: The role of this InlineResponse20030Prefetch.  # noqa: E501
        :rtype: dict(str, Role)
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse20030Prefetch.


        :param role: The role of this InlineResponse20030Prefetch.  # noqa: E501
        :type: dict(str, Role)
        """

        self._role = role

    @property
    def user(self):
        """Gets the user of this InlineResponse20030Prefetch.  # noqa: E501


        :return: The user of this InlineResponse20030Prefetch.  # noqa: E501
        :rtype: dict(str, UserStub)
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineResponse20030Prefetch.


        :param user: The user of this InlineResponse20030Prefetch.  # noqa: E501
        :type: dict(str, UserStub)
        """

        self._user = user

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
        if not isinstance(other, InlineResponse20030Prefetch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20030Prefetch):
            return True

        return self.to_dict() != other.to_dict()
