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


class InlineResponse20032Prefetch(object):
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
        'group': 'dict(str, DojoGroup)',
        'product_type': 'dict(str, ProductType)',
        'role': 'dict(str, Role)'
    }

    attribute_map = {
        'group': 'group',
        'product_type': 'product_type',
        'role': 'role'
    }

    def __init__(self, group=None, product_type=None, role=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20032Prefetch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._product_type = None
        self._role = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if product_type is not None:
            self.product_type = product_type
        if role is not None:
            self.role = role

    @property
    def group(self):
        """Gets the group of this InlineResponse20032Prefetch.  # noqa: E501


        :return: The group of this InlineResponse20032Prefetch.  # noqa: E501
        :rtype: dict(str, DojoGroup)
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this InlineResponse20032Prefetch.


        :param group: The group of this InlineResponse20032Prefetch.  # noqa: E501
        :type: dict(str, DojoGroup)
        """

        self._group = group

    @property
    def product_type(self):
        """Gets the product_type of this InlineResponse20032Prefetch.  # noqa: E501


        :return: The product_type of this InlineResponse20032Prefetch.  # noqa: E501
        :rtype: dict(str, ProductType)
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this InlineResponse20032Prefetch.


        :param product_type: The product_type of this InlineResponse20032Prefetch.  # noqa: E501
        :type: dict(str, ProductType)
        """

        self._product_type = product_type

    @property
    def role(self):
        """Gets the role of this InlineResponse20032Prefetch.  # noqa: E501


        :return: The role of this InlineResponse20032Prefetch.  # noqa: E501
        :rtype: dict(str, Role)
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse20032Prefetch.


        :param role: The role of this InlineResponse20032Prefetch.  # noqa: E501
        :type: dict(str, Role)
        """

        self._role = role

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
        if not isinstance(other, InlineResponse20032Prefetch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20032Prefetch):
            return True

        return self.to_dict() != other.to_dict()