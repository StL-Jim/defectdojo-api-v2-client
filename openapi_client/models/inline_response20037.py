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


class InlineResponse20037(object):
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
        'name': 'str',
        'description': 'str',
        'critical_product': 'bool',
        'key_product': 'bool',
        'updated': 'datetime',
        'created': 'datetime',
        'members': 'list[int]',
        'authorization_groups': 'list[int]',
        'prefetch': 'InlineResponse20036Prefetch'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'critical_product': 'critical_product',
        'key_product': 'key_product',
        'updated': 'updated',
        'created': 'created',
        'members': 'members',
        'authorization_groups': 'authorization_groups',
        'prefetch': 'prefetch'
    }

    def __init__(self, id=None, name=None, description=None, critical_product=None, key_product=None, updated=None, created=None, members=None, authorization_groups=None, prefetch=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20037 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._critical_product = None
        self._key_product = None
        self._updated = None
        self._created = None
        self._members = None
        self._authorization_groups = None
        self._prefetch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        if critical_product is not None:
            self.critical_product = critical_product
        if key_product is not None:
            self.key_product = key_product
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if members is not None:
            self.members = members
        if authorization_groups is not None:
            self.authorization_groups = authorization_groups
        if prefetch is not None:
            self.prefetch = prefetch

    @property
    def id(self):
        """Gets the id of this InlineResponse20037.  # noqa: E501


        :return: The id of this InlineResponse20037.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20037.


        :param id: The id of this InlineResponse20037.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20037.  # noqa: E501


        :return: The name of this InlineResponse20037.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20037.


        :param name: The name of this InlineResponse20037.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InlineResponse20037.  # noqa: E501


        :return: The description of this InlineResponse20037.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20037.


        :param description: The description of this InlineResponse20037.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 4000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4000`")  # noqa: E501

        self._description = description

    @property
    def critical_product(self):
        """Gets the critical_product of this InlineResponse20037.  # noqa: E501


        :return: The critical_product of this InlineResponse20037.  # noqa: E501
        :rtype: bool
        """
        return self._critical_product

    @critical_product.setter
    def critical_product(self, critical_product):
        """Sets the critical_product of this InlineResponse20037.


        :param critical_product: The critical_product of this InlineResponse20037.  # noqa: E501
        :type: bool
        """

        self._critical_product = critical_product

    @property
    def key_product(self):
        """Gets the key_product of this InlineResponse20037.  # noqa: E501


        :return: The key_product of this InlineResponse20037.  # noqa: E501
        :rtype: bool
        """
        return self._key_product

    @key_product.setter
    def key_product(self, key_product):
        """Sets the key_product of this InlineResponse20037.


        :param key_product: The key_product of this InlineResponse20037.  # noqa: E501
        :type: bool
        """

        self._key_product = key_product

    @property
    def updated(self):
        """Gets the updated of this InlineResponse20037.  # noqa: E501


        :return: The updated of this InlineResponse20037.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this InlineResponse20037.


        :param updated: The updated of this InlineResponse20037.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this InlineResponse20037.  # noqa: E501


        :return: The created of this InlineResponse20037.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InlineResponse20037.


        :param created: The created of this InlineResponse20037.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def members(self):
        """Gets the members of this InlineResponse20037.  # noqa: E501


        :return: The members of this InlineResponse20037.  # noqa: E501
        :rtype: list[int]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this InlineResponse20037.


        :param members: The members of this InlineResponse20037.  # noqa: E501
        :type: list[int]
        """

        self._members = members

    @property
    def authorization_groups(self):
        """Gets the authorization_groups of this InlineResponse20037.  # noqa: E501


        :return: The authorization_groups of this InlineResponse20037.  # noqa: E501
        :rtype: list[int]
        """
        return self._authorization_groups

    @authorization_groups.setter
    def authorization_groups(self, authorization_groups):
        """Sets the authorization_groups of this InlineResponse20037.


        :param authorization_groups: The authorization_groups of this InlineResponse20037.  # noqa: E501
        :type: list[int]
        """

        self._authorization_groups = authorization_groups

    @property
    def prefetch(self):
        """Gets the prefetch of this InlineResponse20037.  # noqa: E501


        :return: The prefetch of this InlineResponse20037.  # noqa: E501
        :rtype: InlineResponse20036Prefetch
        """
        return self._prefetch

    @prefetch.setter
    def prefetch(self, prefetch):
        """Sets the prefetch of this InlineResponse20037.


        :param prefetch: The prefetch of this InlineResponse20037.  # noqa: E501
        :type: InlineResponse20036Prefetch
        """

        self._prefetch = prefetch

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
        if not isinstance(other, InlineResponse20037):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20037):
            return True

        return self.to_dict() != other.to_dict()