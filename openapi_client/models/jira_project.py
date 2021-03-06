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


class JIRAProject(object):
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
        'project_key': 'str',
        'issue_template_dir': 'str',
        'component': 'str',
        'push_all_issues': 'bool',
        'enable_engagement_epic_mapping': 'bool',
        'push_notes': 'bool',
        'product_jira_sla_notification': 'bool',
        'risk_acceptance_expiration_notification': 'bool',
        'jira_instance': 'int',
        'product': 'int',
        'engagement': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_key': 'project_key',
        'issue_template_dir': 'issue_template_dir',
        'component': 'component',
        'push_all_issues': 'push_all_issues',
        'enable_engagement_epic_mapping': 'enable_engagement_epic_mapping',
        'push_notes': 'push_notes',
        'product_jira_sla_notification': 'product_jira_sla_notification',
        'risk_acceptance_expiration_notification': 'risk_acceptance_expiration_notification',
        'jira_instance': 'jira_instance',
        'product': 'product',
        'engagement': 'engagement'
    }

    def __init__(self, id=None, project_key=None, issue_template_dir=None, component=None, push_all_issues=None, enable_engagement_epic_mapping=None, push_notes=None, product_jira_sla_notification=None, risk_acceptance_expiration_notification=None, jira_instance=None, product=None, engagement=None, local_vars_configuration=None):  # noqa: E501
        """JIRAProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._project_key = None
        self._issue_template_dir = None
        self._component = None
        self._push_all_issues = None
        self._enable_engagement_epic_mapping = None
        self._push_notes = None
        self._product_jira_sla_notification = None
        self._risk_acceptance_expiration_notification = None
        self._jira_instance = None
        self._product = None
        self._engagement = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_key is not None:
            self.project_key = project_key
        self.issue_template_dir = issue_template_dir
        if component is not None:
            self.component = component
        if push_all_issues is not None:
            self.push_all_issues = push_all_issues
        if enable_engagement_epic_mapping is not None:
            self.enable_engagement_epic_mapping = enable_engagement_epic_mapping
        if push_notes is not None:
            self.push_notes = push_notes
        if product_jira_sla_notification is not None:
            self.product_jira_sla_notification = product_jira_sla_notification
        if risk_acceptance_expiration_notification is not None:
            self.risk_acceptance_expiration_notification = risk_acceptance_expiration_notification
        self.jira_instance = jira_instance
        self.product = product
        self.engagement = engagement

    @property
    def id(self):
        """Gets the id of this JIRAProject.  # noqa: E501


        :return: The id of this JIRAProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JIRAProject.


        :param id: The id of this JIRAProject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_key(self):
        """Gets the project_key of this JIRAProject.  # noqa: E501


        :return: The project_key of this JIRAProject.  # noqa: E501
        :rtype: str
        """
        return self._project_key

    @project_key.setter
    def project_key(self, project_key):
        """Sets the project_key of this JIRAProject.


        :param project_key: The project_key of this JIRAProject.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                project_key is not None and len(project_key) > 200):
            raise ValueError("Invalid value for `project_key`, length must be less than or equal to `200`")  # noqa: E501

        self._project_key = project_key

    @property
    def issue_template_dir(self):
        """Gets the issue_template_dir of this JIRAProject.  # noqa: E501

        Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.  # noqa: E501

        :return: The issue_template_dir of this JIRAProject.  # noqa: E501
        :rtype: str
        """
        return self._issue_template_dir

    @issue_template_dir.setter
    def issue_template_dir(self, issue_template_dir):
        """Sets the issue_template_dir of this JIRAProject.

        Choose the folder containing the Django templates used to render the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default jira_full templates.  # noqa: E501

        :param issue_template_dir: The issue_template_dir of this JIRAProject.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                issue_template_dir is not None and len(issue_template_dir) > 255):
            raise ValueError("Invalid value for `issue_template_dir`, length must be less than or equal to `255`")  # noqa: E501

        self._issue_template_dir = issue_template_dir

    @property
    def component(self):
        """Gets the component of this JIRAProject.  # noqa: E501


        :return: The component of this JIRAProject.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this JIRAProject.


        :param component: The component of this JIRAProject.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                component is not None and len(component) > 200):
            raise ValueError("Invalid value for `component`, length must be less than or equal to `200`")  # noqa: E501

        self._component = component

    @property
    def push_all_issues(self):
        """Gets the push_all_issues of this JIRAProject.  # noqa: E501

        Automatically maintain parity with JIRA. Always create and update JIRA tickets for findings in this Product.  # noqa: E501

        :return: The push_all_issues of this JIRAProject.  # noqa: E501
        :rtype: bool
        """
        return self._push_all_issues

    @push_all_issues.setter
    def push_all_issues(self, push_all_issues):
        """Sets the push_all_issues of this JIRAProject.

        Automatically maintain parity with JIRA. Always create and update JIRA tickets for findings in this Product.  # noqa: E501

        :param push_all_issues: The push_all_issues of this JIRAProject.  # noqa: E501
        :type: bool
        """

        self._push_all_issues = push_all_issues

    @property
    def enable_engagement_epic_mapping(self):
        """Gets the enable_engagement_epic_mapping of this JIRAProject.  # noqa: E501


        :return: The enable_engagement_epic_mapping of this JIRAProject.  # noqa: E501
        :rtype: bool
        """
        return self._enable_engagement_epic_mapping

    @enable_engagement_epic_mapping.setter
    def enable_engagement_epic_mapping(self, enable_engagement_epic_mapping):
        """Sets the enable_engagement_epic_mapping of this JIRAProject.


        :param enable_engagement_epic_mapping: The enable_engagement_epic_mapping of this JIRAProject.  # noqa: E501
        :type: bool
        """

        self._enable_engagement_epic_mapping = enable_engagement_epic_mapping

    @property
    def push_notes(self):
        """Gets the push_notes of this JIRAProject.  # noqa: E501


        :return: The push_notes of this JIRAProject.  # noqa: E501
        :rtype: bool
        """
        return self._push_notes

    @push_notes.setter
    def push_notes(self, push_notes):
        """Sets the push_notes of this JIRAProject.


        :param push_notes: The push_notes of this JIRAProject.  # noqa: E501
        :type: bool
        """

        self._push_notes = push_notes

    @property
    def product_jira_sla_notification(self):
        """Gets the product_jira_sla_notification of this JIRAProject.  # noqa: E501


        :return: The product_jira_sla_notification of this JIRAProject.  # noqa: E501
        :rtype: bool
        """
        return self._product_jira_sla_notification

    @product_jira_sla_notification.setter
    def product_jira_sla_notification(self, product_jira_sla_notification):
        """Sets the product_jira_sla_notification of this JIRAProject.


        :param product_jira_sla_notification: The product_jira_sla_notification of this JIRAProject.  # noqa: E501
        :type: bool
        """

        self._product_jira_sla_notification = product_jira_sla_notification

    @property
    def risk_acceptance_expiration_notification(self):
        """Gets the risk_acceptance_expiration_notification of this JIRAProject.  # noqa: E501


        :return: The risk_acceptance_expiration_notification of this JIRAProject.  # noqa: E501
        :rtype: bool
        """
        return self._risk_acceptance_expiration_notification

    @risk_acceptance_expiration_notification.setter
    def risk_acceptance_expiration_notification(self, risk_acceptance_expiration_notification):
        """Sets the risk_acceptance_expiration_notification of this JIRAProject.


        :param risk_acceptance_expiration_notification: The risk_acceptance_expiration_notification of this JIRAProject.  # noqa: E501
        :type: bool
        """

        self._risk_acceptance_expiration_notification = risk_acceptance_expiration_notification

    @property
    def jira_instance(self):
        """Gets the jira_instance of this JIRAProject.  # noqa: E501


        :return: The jira_instance of this JIRAProject.  # noqa: E501
        :rtype: int
        """
        return self._jira_instance

    @jira_instance.setter
    def jira_instance(self, jira_instance):
        """Sets the jira_instance of this JIRAProject.


        :param jira_instance: The jira_instance of this JIRAProject.  # noqa: E501
        :type: int
        """

        self._jira_instance = jira_instance

    @property
    def product(self):
        """Gets the product of this JIRAProject.  # noqa: E501


        :return: The product of this JIRAProject.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this JIRAProject.


        :param product: The product of this JIRAProject.  # noqa: E501
        :type: int
        """

        self._product = product

    @property
    def engagement(self):
        """Gets the engagement of this JIRAProject.  # noqa: E501


        :return: The engagement of this JIRAProject.  # noqa: E501
        :rtype: int
        """
        return self._engagement

    @engagement.setter
    def engagement(self, engagement):
        """Sets the engagement of this JIRAProject.


        :param engagement: The engagement of this JIRAProject.  # noqa: E501
        :type: int
        """

        self._engagement = engagement

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
        if not isinstance(other, JIRAProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JIRAProject):
            return True

        return self.to_dict() != other.to_dict()
