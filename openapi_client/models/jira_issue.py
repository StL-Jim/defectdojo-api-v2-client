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


class JIRAIssue(object):
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
        'url': 'str',
        'jira_id': 'str',
        'jira_key': 'str',
        'jira_creation': 'datetime',
        'jira_change': 'datetime',
        'jira_project': 'int',
        'finding': 'int',
        'engagement': 'int',
        'finding_group': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'jira_id': 'jira_id',
        'jira_key': 'jira_key',
        'jira_creation': 'jira_creation',
        'jira_change': 'jira_change',
        'jira_project': 'jira_project',
        'finding': 'finding',
        'engagement': 'engagement',
        'finding_group': 'finding_group'
    }

    def __init__(self, id=None, url=None, jira_id=None, jira_key=None, jira_creation=None, jira_change=None, jira_project=None, finding=None, engagement=None, finding_group=None, local_vars_configuration=None):  # noqa: E501
        """JIRAIssue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._url = None
        self._jira_id = None
        self._jira_key = None
        self._jira_creation = None
        self._jira_change = None
        self._jira_project = None
        self._finding = None
        self._engagement = None
        self._finding_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.jira_id = jira_id
        self.jira_key = jira_key
        self.jira_creation = jira_creation
        self.jira_change = jira_change
        self.jira_project = jira_project
        self.finding = finding
        self.engagement = engagement
        self.finding_group = finding_group

    @property
    def id(self):
        """Gets the id of this JIRAIssue.  # noqa: E501


        :return: The id of this JIRAIssue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JIRAIssue.


        :param id: The id of this JIRAIssue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this JIRAIssue.  # noqa: E501


        :return: The url of this JIRAIssue.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this JIRAIssue.


        :param url: The url of this JIRAIssue.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def jira_id(self):
        """Gets the jira_id of this JIRAIssue.  # noqa: E501


        :return: The jira_id of this JIRAIssue.  # noqa: E501
        :rtype: str
        """
        return self._jira_id

    @jira_id.setter
    def jira_id(self, jira_id):
        """Sets the jira_id of this JIRAIssue.


        :param jira_id: The jira_id of this JIRAIssue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jira_id is None:  # noqa: E501
            raise ValueError("Invalid value for `jira_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                jira_id is not None and len(jira_id) > 200):
            raise ValueError("Invalid value for `jira_id`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                jira_id is not None and len(jira_id) < 1):
            raise ValueError("Invalid value for `jira_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._jira_id = jira_id

    @property
    def jira_key(self):
        """Gets the jira_key of this JIRAIssue.  # noqa: E501


        :return: The jira_key of this JIRAIssue.  # noqa: E501
        :rtype: str
        """
        return self._jira_key

    @jira_key.setter
    def jira_key(self, jira_key):
        """Sets the jira_key of this JIRAIssue.


        :param jira_key: The jira_key of this JIRAIssue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jira_key is None:  # noqa: E501
            raise ValueError("Invalid value for `jira_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                jira_key is not None and len(jira_key) > 200):
            raise ValueError("Invalid value for `jira_key`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                jira_key is not None and len(jira_key) < 1):
            raise ValueError("Invalid value for `jira_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._jira_key = jira_key

    @property
    def jira_creation(self):
        """Gets the jira_creation of this JIRAIssue.  # noqa: E501

        The date a Jira issue was created from this finding.  # noqa: E501

        :return: The jira_creation of this JIRAIssue.  # noqa: E501
        :rtype: datetime
        """
        return self._jira_creation

    @jira_creation.setter
    def jira_creation(self, jira_creation):
        """Sets the jira_creation of this JIRAIssue.

        The date a Jira issue was created from this finding.  # noqa: E501

        :param jira_creation: The jira_creation of this JIRAIssue.  # noqa: E501
        :type: datetime
        """

        self._jira_creation = jira_creation

    @property
    def jira_change(self):
        """Gets the jira_change of this JIRAIssue.  # noqa: E501

        The date the linked Jira issue was last modified.  # noqa: E501

        :return: The jira_change of this JIRAIssue.  # noqa: E501
        :rtype: datetime
        """
        return self._jira_change

    @jira_change.setter
    def jira_change(self, jira_change):
        """Sets the jira_change of this JIRAIssue.

        The date the linked Jira issue was last modified.  # noqa: E501

        :param jira_change: The jira_change of this JIRAIssue.  # noqa: E501
        :type: datetime
        """

        self._jira_change = jira_change

    @property
    def jira_project(self):
        """Gets the jira_project of this JIRAIssue.  # noqa: E501


        :return: The jira_project of this JIRAIssue.  # noqa: E501
        :rtype: int
        """
        return self._jira_project

    @jira_project.setter
    def jira_project(self, jira_project):
        """Sets the jira_project of this JIRAIssue.


        :param jira_project: The jira_project of this JIRAIssue.  # noqa: E501
        :type: int
        """

        self._jira_project = jira_project

    @property
    def finding(self):
        """Gets the finding of this JIRAIssue.  # noqa: E501


        :return: The finding of this JIRAIssue.  # noqa: E501
        :rtype: int
        """
        return self._finding

    @finding.setter
    def finding(self, finding):
        """Sets the finding of this JIRAIssue.


        :param finding: The finding of this JIRAIssue.  # noqa: E501
        :type: int
        """

        self._finding = finding

    @property
    def engagement(self):
        """Gets the engagement of this JIRAIssue.  # noqa: E501


        :return: The engagement of this JIRAIssue.  # noqa: E501
        :rtype: int
        """
        return self._engagement

    @engagement.setter
    def engagement(self, engagement):
        """Sets the engagement of this JIRAIssue.


        :param engagement: The engagement of this JIRAIssue.  # noqa: E501
        :type: int
        """

        self._engagement = engagement

    @property
    def finding_group(self):
        """Gets the finding_group of this JIRAIssue.  # noqa: E501


        :return: The finding_group of this JIRAIssue.  # noqa: E501
        :rtype: int
        """
        return self._finding_group

    @finding_group.setter
    def finding_group(self, finding_group):
        """Sets the finding_group of this JIRAIssue.


        :param finding_group: The finding_group of this JIRAIssue.  # noqa: E501
        :type: int
        """

        self._finding_group = finding_group

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
        if not isinstance(other, JIRAIssue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JIRAIssue):
            return True

        return self.to_dict() != other.to_dict()