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


class InlineResponse20020Prefetch(object):
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
        'endpoint': 'dict(str, Endpoint)',
        'finding': 'dict(str, Finding)',
        'product': 'dict(str, Product)'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'finding': 'finding',
        'product': 'product'
    }

    def __init__(self, endpoint=None, finding=None, product=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20020Prefetch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._endpoint = None
        self._finding = None
        self._product = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if finding is not None:
            self.finding = finding
        if product is not None:
            self.product = product

    @property
    def endpoint(self):
        """Gets the endpoint of this InlineResponse20020Prefetch.  # noqa: E501


        :return: The endpoint of this InlineResponse20020Prefetch.  # noqa: E501
        :rtype: dict(str, Endpoint)
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this InlineResponse20020Prefetch.


        :param endpoint: The endpoint of this InlineResponse20020Prefetch.  # noqa: E501
        :type: dict(str, Endpoint)
        """

        self._endpoint = endpoint

    @property
    def finding(self):
        """Gets the finding of this InlineResponse20020Prefetch.  # noqa: E501


        :return: The finding of this InlineResponse20020Prefetch.  # noqa: E501
        :rtype: dict(str, Finding)
        """
        return self._finding

    @finding.setter
    def finding(self, finding):
        """Sets the finding of this InlineResponse20020Prefetch.


        :param finding: The finding of this InlineResponse20020Prefetch.  # noqa: E501
        :type: dict(str, Finding)
        """

        self._finding = finding

    @property
    def product(self):
        """Gets the product of this InlineResponse20020Prefetch.  # noqa: E501


        :return: The product of this InlineResponse20020Prefetch.  # noqa: E501
        :rtype: dict(str, Product)
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InlineResponse20020Prefetch.


        :param product: The product of this InlineResponse20020Prefetch.  # noqa: E501
        :type: dict(str, Product)
        """

        self._product = product

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
        if not isinstance(other, InlineResponse20020Prefetch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20020Prefetch):
            return True

        return self.to_dict() != other.to_dict()
