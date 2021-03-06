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


class EngagementToNotes(object):
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
        'engagement_id': 'int',
        'notes': 'list[Note]'
    }

    attribute_map = {
        'engagement_id': 'engagement_id',
        'notes': 'notes'
    }

    def __init__(self, engagement_id=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """EngagementToNotes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._engagement_id = None
        self._notes = None
        self.discriminator = None

        self.engagement_id = engagement_id
        self.notes = notes

    @property
    def engagement_id(self):
        """Gets the engagement_id of this EngagementToNotes.  # noqa: E501


        :return: The engagement_id of this EngagementToNotes.  # noqa: E501
        :rtype: int
        """
        return self._engagement_id

    @engagement_id.setter
    def engagement_id(self, engagement_id):
        """Sets the engagement_id of this EngagementToNotes.


        :param engagement_id: The engagement_id of this EngagementToNotes.  # noqa: E501
        :type: int
        """

        self._engagement_id = engagement_id

    @property
    def notes(self):
        """Gets the notes of this EngagementToNotes.  # noqa: E501


        :return: The notes of this EngagementToNotes.  # noqa: E501
        :rtype: list[Note]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EngagementToNotes.


        :param notes: The notes of this EngagementToNotes.  # noqa: E501
        :type: list[Note]
        """
        if self.local_vars_configuration.client_side_validation and notes is None:  # noqa: E501
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

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
        if not isinstance(other, EngagementToNotes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EngagementToNotes):
            return True

        return self.to_dict() != other.to_dict()
