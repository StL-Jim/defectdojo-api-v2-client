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


class UserProfile(object):
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
        'user': 'User',
        'user_contact_info': 'UserContactInfo',
        'global_role': 'GlobalRole',
        'dojo_group_member': 'list[DojoGroupMember]',
        'product_type_member': 'list[ProductTypeMember]',
        'product_member': 'list[ProductMember]'
    }

    attribute_map = {
        'user': 'user',
        'user_contact_info': 'user_contact_info',
        'global_role': 'global_role',
        'dojo_group_member': 'dojo_group_member',
        'product_type_member': 'product_type_member',
        'product_member': 'product_member'
    }

    def __init__(self, user=None, user_contact_info=None, global_role=None, dojo_group_member=None, product_type_member=None, product_member=None, local_vars_configuration=None):  # noqa: E501
        """UserProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._user_contact_info = None
        self._global_role = None
        self._dojo_group_member = None
        self._product_type_member = None
        self._product_member = None
        self.discriminator = None

        self.user = user
        self.user_contact_info = user_contact_info
        self.global_role = global_role
        self.dojo_group_member = dojo_group_member
        self.product_type_member = product_type_member
        self.product_member = product_member

    @property
    def user(self):
        """Gets the user of this UserProfile.  # noqa: E501


        :return: The user of this UserProfile.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserProfile.


        :param user: The user of this UserProfile.  # noqa: E501
        :type: User
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def user_contact_info(self):
        """Gets the user_contact_info of this UserProfile.  # noqa: E501


        :return: The user_contact_info of this UserProfile.  # noqa: E501
        :rtype: UserContactInfo
        """
        return self._user_contact_info

    @user_contact_info.setter
    def user_contact_info(self, user_contact_info):
        """Sets the user_contact_info of this UserProfile.


        :param user_contact_info: The user_contact_info of this UserProfile.  # noqa: E501
        :type: UserContactInfo
        """
        if self.local_vars_configuration.client_side_validation and user_contact_info is None:  # noqa: E501
            raise ValueError("Invalid value for `user_contact_info`, must not be `None`")  # noqa: E501

        self._user_contact_info = user_contact_info

    @property
    def global_role(self):
        """Gets the global_role of this UserProfile.  # noqa: E501


        :return: The global_role of this UserProfile.  # noqa: E501
        :rtype: GlobalRole
        """
        return self._global_role

    @global_role.setter
    def global_role(self, global_role):
        """Sets the global_role of this UserProfile.


        :param global_role: The global_role of this UserProfile.  # noqa: E501
        :type: GlobalRole
        """
        if self.local_vars_configuration.client_side_validation and global_role is None:  # noqa: E501
            raise ValueError("Invalid value for `global_role`, must not be `None`")  # noqa: E501

        self._global_role = global_role

    @property
    def dojo_group_member(self):
        """Gets the dojo_group_member of this UserProfile.  # noqa: E501


        :return: The dojo_group_member of this UserProfile.  # noqa: E501
        :rtype: list[DojoGroupMember]
        """
        return self._dojo_group_member

    @dojo_group_member.setter
    def dojo_group_member(self, dojo_group_member):
        """Sets the dojo_group_member of this UserProfile.


        :param dojo_group_member: The dojo_group_member of this UserProfile.  # noqa: E501
        :type: list[DojoGroupMember]
        """
        if self.local_vars_configuration.client_side_validation and dojo_group_member is None:  # noqa: E501
            raise ValueError("Invalid value for `dojo_group_member`, must not be `None`")  # noqa: E501

        self._dojo_group_member = dojo_group_member

    @property
    def product_type_member(self):
        """Gets the product_type_member of this UserProfile.  # noqa: E501


        :return: The product_type_member of this UserProfile.  # noqa: E501
        :rtype: list[ProductTypeMember]
        """
        return self._product_type_member

    @product_type_member.setter
    def product_type_member(self, product_type_member):
        """Sets the product_type_member of this UserProfile.


        :param product_type_member: The product_type_member of this UserProfile.  # noqa: E501
        :type: list[ProductTypeMember]
        """
        if self.local_vars_configuration.client_side_validation and product_type_member is None:  # noqa: E501
            raise ValueError("Invalid value for `product_type_member`, must not be `None`")  # noqa: E501

        self._product_type_member = product_type_member

    @property
    def product_member(self):
        """Gets the product_member of this UserProfile.  # noqa: E501


        :return: The product_member of this UserProfile.  # noqa: E501
        :rtype: list[ProductMember]
        """
        return self._product_member

    @product_member.setter
    def product_member(self, product_member):
        """Sets the product_member of this UserProfile.


        :param product_member: The product_member of this UserProfile.  # noqa: E501
        :type: list[ProductMember]
        """
        if self.local_vars_configuration.client_side_validation and product_member is None:  # noqa: E501
            raise ValueError("Invalid value for `product_member`, must not be `None`")  # noqa: E501

        self._product_member = product_member

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
        if not isinstance(other, UserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfile):
            return True

        return self.to_dict() != other.to_dict()