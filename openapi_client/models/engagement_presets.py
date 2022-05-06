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


class EngagementPresets(object):
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
        'title': 'str',
        'notes': 'str',
        'scope': 'str',
        'created': 'datetime',
        'product': 'int',
        'test_type': 'list[int]',
        'network_locations': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'notes': 'notes',
        'scope': 'scope',
        'created': 'created',
        'product': 'product',
        'test_type': 'test_type',
        'network_locations': 'network_locations'
    }

    def __init__(self, id=None, title=None, notes=None, scope=None, created=None, product=None, test_type=None, network_locations=None, local_vars_configuration=None):  # noqa: E501
        """EngagementPresets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._notes = None
        self._scope = None
        self._created = None
        self._product = None
        self._test_type = None
        self._network_locations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        self.notes = notes
        if scope is not None:
            self.scope = scope
        if created is not None:
            self.created = created
        self.product = product
        if test_type is not None:
            self.test_type = test_type
        if network_locations is not None:
            self.network_locations = network_locations

    @property
    def id(self):
        """Gets the id of this EngagementPresets.  # noqa: E501


        :return: The id of this EngagementPresets.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EngagementPresets.


        :param id: The id of this EngagementPresets.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this EngagementPresets.  # noqa: E501

        Brief description of preset.  # noqa: E501

        :return: The title of this EngagementPresets.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EngagementPresets.

        Brief description of preset.  # noqa: E501

        :param title: The title of this EngagementPresets.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 500):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def notes(self):
        """Gets the notes of this EngagementPresets.  # noqa: E501

        Description of what needs to be tested or setting up environment for testing  # noqa: E501

        :return: The notes of this EngagementPresets.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EngagementPresets.

        Description of what needs to be tested or setting up environment for testing  # noqa: E501

        :param notes: The notes of this EngagementPresets.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 2000):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `2000`")  # noqa: E501

        self._notes = notes

    @property
    def scope(self):
        """Gets the scope of this EngagementPresets.  # noqa: E501

        Scope of Engagement testing, IP's/Resources/URL's)  # noqa: E501

        :return: The scope of this EngagementPresets.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this EngagementPresets.

        Scope of Engagement testing, IP's/Resources/URL's)  # noqa: E501

        :param scope: The scope of this EngagementPresets.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 800):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `800`")  # noqa: E501

        self._scope = scope

    @property
    def created(self):
        """Gets the created of this EngagementPresets.  # noqa: E501


        :return: The created of this EngagementPresets.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EngagementPresets.


        :param created: The created of this EngagementPresets.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def product(self):
        """Gets the product of this EngagementPresets.  # noqa: E501


        :return: The product of this EngagementPresets.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this EngagementPresets.


        :param product: The product of this EngagementPresets.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def test_type(self):
        """Gets the test_type of this EngagementPresets.  # noqa: E501


        :return: The test_type of this EngagementPresets.  # noqa: E501
        :rtype: list[int]
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this EngagementPresets.


        :param test_type: The test_type of this EngagementPresets.  # noqa: E501
        :type: list[int]
        """

        self._test_type = test_type

    @property
    def network_locations(self):
        """Gets the network_locations of this EngagementPresets.  # noqa: E501


        :return: The network_locations of this EngagementPresets.  # noqa: E501
        :rtype: list[int]
        """
        return self._network_locations

    @network_locations.setter
    def network_locations(self, network_locations):
        """Sets the network_locations of this EngagementPresets.


        :param network_locations: The network_locations of this EngagementPresets.  # noqa: E501
        :type: list[int]
        """

        self._network_locations = network_locations

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
        if not isinstance(other, EngagementPresets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EngagementPresets):
            return True

        return self.to_dict() != other.to_dict()
