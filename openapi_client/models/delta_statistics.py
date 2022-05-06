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


class DeltaStatistics(object):
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
        'created': 'SeverityStatusStatistics',
        'closed': 'SeverityStatusStatistics',
        'reactivated': 'SeverityStatusStatistics',
        'left_untouched': 'SeverityStatusStatistics'
    }

    attribute_map = {
        'created': 'created',
        'closed': 'closed',
        'reactivated': 'reactivated',
        'left_untouched': 'left untouched'
    }

    def __init__(self, created=None, closed=None, reactivated=None, left_untouched=None, local_vars_configuration=None):  # noqa: E501
        """DeltaStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._closed = None
        self._reactivated = None
        self._left_untouched = None
        self.discriminator = None

        self.created = created
        self.closed = closed
        self.reactivated = reactivated
        self.left_untouched = left_untouched

    @property
    def created(self):
        """Gets the created of this DeltaStatistics.  # noqa: E501


        :return: The created of this DeltaStatistics.  # noqa: E501
        :rtype: SeverityStatusStatistics
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DeltaStatistics.


        :param created: The created of this DeltaStatistics.  # noqa: E501
        :type: SeverityStatusStatistics
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def closed(self):
        """Gets the closed of this DeltaStatistics.  # noqa: E501


        :return: The closed of this DeltaStatistics.  # noqa: E501
        :rtype: SeverityStatusStatistics
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this DeltaStatistics.


        :param closed: The closed of this DeltaStatistics.  # noqa: E501
        :type: SeverityStatusStatistics
        """
        if self.local_vars_configuration.client_side_validation and closed is None:  # noqa: E501
            raise ValueError("Invalid value for `closed`, must not be `None`")  # noqa: E501

        self._closed = closed

    @property
    def reactivated(self):
        """Gets the reactivated of this DeltaStatistics.  # noqa: E501


        :return: The reactivated of this DeltaStatistics.  # noqa: E501
        :rtype: SeverityStatusStatistics
        """
        return self._reactivated

    @reactivated.setter
    def reactivated(self, reactivated):
        """Sets the reactivated of this DeltaStatistics.


        :param reactivated: The reactivated of this DeltaStatistics.  # noqa: E501
        :type: SeverityStatusStatistics
        """
        if self.local_vars_configuration.client_side_validation and reactivated is None:  # noqa: E501
            raise ValueError("Invalid value for `reactivated`, must not be `None`")  # noqa: E501

        self._reactivated = reactivated

    @property
    def left_untouched(self):
        """Gets the left_untouched of this DeltaStatistics.  # noqa: E501


        :return: The left_untouched of this DeltaStatistics.  # noqa: E501
        :rtype: SeverityStatusStatistics
        """
        return self._left_untouched

    @left_untouched.setter
    def left_untouched(self, left_untouched):
        """Sets the left_untouched of this DeltaStatistics.


        :param left_untouched: The left_untouched of this DeltaStatistics.  # noqa: E501
        :type: SeverityStatusStatistics
        """
        if self.local_vars_configuration.client_side_validation and left_untouched is None:  # noqa: E501
            raise ValueError("Invalid value for `left_untouched`, must not be `None`")  # noqa: E501

        self._left_untouched = left_untouched

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
        if not isinstance(other, DeltaStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeltaStatistics):
            return True

        return self.to_dict() != other.to_dict()