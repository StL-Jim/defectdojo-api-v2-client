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


class InlineResponse20038Prefetch(object):
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
        'authorization_groups': 'dict(str, DojoGroup)',
        'members': 'dict(str, UserStub)',
        'prod_type': 'dict(str, ProductType)',
        'product_manager': 'dict(str, UserStub)',
        'regulations': 'dict(str, Regulation)',
        'team_manager': 'dict(str, UserStub)',
        'technical_contact': 'dict(str, UserStub)'
    }

    attribute_map = {
        'authorization_groups': 'authorization_groups',
        'members': 'members',
        'prod_type': 'prod_type',
        'product_manager': 'product_manager',
        'regulations': 'regulations',
        'team_manager': 'team_manager',
        'technical_contact': 'technical_contact'
    }

    def __init__(self, authorization_groups=None, members=None, prod_type=None, product_manager=None, regulations=None, team_manager=None, technical_contact=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20038Prefetch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorization_groups = None
        self._members = None
        self._prod_type = None
        self._product_manager = None
        self._regulations = None
        self._team_manager = None
        self._technical_contact = None
        self.discriminator = None

        if authorization_groups is not None:
            self.authorization_groups = authorization_groups
        if members is not None:
            self.members = members
        if prod_type is not None:
            self.prod_type = prod_type
        if product_manager is not None:
            self.product_manager = product_manager
        if regulations is not None:
            self.regulations = regulations
        if team_manager is not None:
            self.team_manager = team_manager
        if technical_contact is not None:
            self.technical_contact = technical_contact

    @property
    def authorization_groups(self):
        """Gets the authorization_groups of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The authorization_groups of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, DojoGroup)
        """
        return self._authorization_groups

    @authorization_groups.setter
    def authorization_groups(self, authorization_groups):
        """Sets the authorization_groups of this InlineResponse20038Prefetch.


        :param authorization_groups: The authorization_groups of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, DojoGroup)
        """

        self._authorization_groups = authorization_groups

    @property
    def members(self):
        """Gets the members of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The members of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, UserStub)
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this InlineResponse20038Prefetch.


        :param members: The members of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, UserStub)
        """

        self._members = members

    @property
    def prod_type(self):
        """Gets the prod_type of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The prod_type of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, ProductType)
        """
        return self._prod_type

    @prod_type.setter
    def prod_type(self, prod_type):
        """Sets the prod_type of this InlineResponse20038Prefetch.


        :param prod_type: The prod_type of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, ProductType)
        """

        self._prod_type = prod_type

    @property
    def product_manager(self):
        """Gets the product_manager of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The product_manager of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, UserStub)
        """
        return self._product_manager

    @product_manager.setter
    def product_manager(self, product_manager):
        """Sets the product_manager of this InlineResponse20038Prefetch.


        :param product_manager: The product_manager of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, UserStub)
        """

        self._product_manager = product_manager

    @property
    def regulations(self):
        """Gets the regulations of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The regulations of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, Regulation)
        """
        return self._regulations

    @regulations.setter
    def regulations(self, regulations):
        """Sets the regulations of this InlineResponse20038Prefetch.


        :param regulations: The regulations of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, Regulation)
        """

        self._regulations = regulations

    @property
    def team_manager(self):
        """Gets the team_manager of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The team_manager of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, UserStub)
        """
        return self._team_manager

    @team_manager.setter
    def team_manager(self, team_manager):
        """Sets the team_manager of this InlineResponse20038Prefetch.


        :param team_manager: The team_manager of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, UserStub)
        """

        self._team_manager = team_manager

    @property
    def technical_contact(self):
        """Gets the technical_contact of this InlineResponse20038Prefetch.  # noqa: E501


        :return: The technical_contact of this InlineResponse20038Prefetch.  # noqa: E501
        :rtype: dict(str, UserStub)
        """
        return self._technical_contact

    @technical_contact.setter
    def technical_contact(self, technical_contact):
        """Sets the technical_contact of this InlineResponse20038Prefetch.


        :param technical_contact: The technical_contact of this InlineResponse20038Prefetch.  # noqa: E501
        :type: dict(str, UserStub)
        """

        self._technical_contact = technical_contact

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
        if not isinstance(other, InlineResponse20038Prefetch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20038Prefetch):
            return True

        return self.to_dict() != other.to_dict()
