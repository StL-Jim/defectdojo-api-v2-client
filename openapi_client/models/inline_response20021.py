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


class InlineResponse20021(object):
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
        'product': 'int',
        'endpoint': 'int',
        'finding': 'int',
        'name': 'str',
        'value': 'str',
        'prefetch': 'InlineResponse20020Prefetch'
    }

    attribute_map = {
        'id': 'id',
        'product': 'product',
        'endpoint': 'endpoint',
        'finding': 'finding',
        'name': 'name',
        'value': 'value',
        'prefetch': 'prefetch'
    }

    def __init__(self, id=None, product=None, endpoint=None, finding=None, name=None, value=None, prefetch=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20021 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._product = None
        self._endpoint = None
        self._finding = None
        self._name = None
        self._value = None
        self._prefetch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.product = product
        self.endpoint = endpoint
        self.finding = finding
        self.name = name
        self.value = value
        if prefetch is not None:
            self.prefetch = prefetch

    @property
    def id(self):
        """Gets the id of this InlineResponse20021.  # noqa: E501


        :return: The id of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20021.


        :param id: The id of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def product(self):
        """Gets the product of this InlineResponse20021.  # noqa: E501


        :return: The product of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InlineResponse20021.


        :param product: The product of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._product = product

    @property
    def endpoint(self):
        """Gets the endpoint of this InlineResponse20021.  # noqa: E501


        :return: The endpoint of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this InlineResponse20021.


        :param endpoint: The endpoint of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._endpoint = endpoint

    @property
    def finding(self):
        """Gets the finding of this InlineResponse20021.  # noqa: E501


        :return: The finding of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._finding

    @finding.setter
    def finding(self, finding):
        """Sets the finding of this InlineResponse20021.


        :param finding: The finding of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._finding = finding

    @property
    def name(self):
        """Gets the name of this InlineResponse20021.  # noqa: E501


        :return: The name of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20021.


        :param name: The name of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 120):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `120`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this InlineResponse20021.  # noqa: E501


        :return: The value of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse20021.


        :param value: The value of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) > 300):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def prefetch(self):
        """Gets the prefetch of this InlineResponse20021.  # noqa: E501


        :return: The prefetch of this InlineResponse20021.  # noqa: E501
        :rtype: InlineResponse20020Prefetch
        """
        return self._prefetch

    @prefetch.setter
    def prefetch(self, prefetch):
        """Sets the prefetch of this InlineResponse20021.


        :param prefetch: The prefetch of this InlineResponse20021.  # noqa: E501
        :type: InlineResponse20020Prefetch
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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20021):
            return True

        return self.to_dict() != other.to_dict()
