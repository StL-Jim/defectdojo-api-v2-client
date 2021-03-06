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


class RiskAcceptance(object):
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
        'recommendation': 'str',
        'recommendation_details': 'str',
        'decision': 'str',
        'decision_details': 'str',
        'accepted_by': 'str',
        'path': 'str',
        'expiration_date': 'datetime',
        'expiration_date_warned': 'datetime',
        'expiration_date_handled': 'datetime',
        'reactivate_expired': 'bool',
        'restart_sla_expired': 'bool',
        'created': 'datetime',
        'updated': 'datetime',
        'owner': 'int',
        'accepted_findings': 'list[int]',
        'notes': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'recommendation': 'recommendation',
        'recommendation_details': 'recommendation_details',
        'decision': 'decision',
        'decision_details': 'decision_details',
        'accepted_by': 'accepted_by',
        'path': 'path',
        'expiration_date': 'expiration_date',
        'expiration_date_warned': 'expiration_date_warned',
        'expiration_date_handled': 'expiration_date_handled',
        'reactivate_expired': 'reactivate_expired',
        'restart_sla_expired': 'restart_sla_expired',
        'created': 'created',
        'updated': 'updated',
        'owner': 'owner',
        'accepted_findings': 'accepted_findings',
        'notes': 'notes'
    }

    def __init__(self, id=None, name=None, recommendation=None, recommendation_details=None, decision=None, decision_details=None, accepted_by=None, path=None, expiration_date=None, expiration_date_warned=None, expiration_date_handled=None, reactivate_expired=None, restart_sla_expired=None, created=None, updated=None, owner=None, accepted_findings=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """RiskAcceptance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._recommendation = None
        self._recommendation_details = None
        self._decision = None
        self._decision_details = None
        self._accepted_by = None
        self._path = None
        self._expiration_date = None
        self._expiration_date_warned = None
        self._expiration_date_handled = None
        self._reactivate_expired = None
        self._restart_sla_expired = None
        self._created = None
        self._updated = None
        self._owner = None
        self._accepted_findings = None
        self._notes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if recommendation is not None:
            self.recommendation = recommendation
        self.recommendation_details = recommendation_details
        if decision is not None:
            self.decision = decision
        self.decision_details = decision_details
        self.accepted_by = accepted_by
        self.path = path
        self.expiration_date = expiration_date
        self.expiration_date_warned = expiration_date_warned
        self.expiration_date_handled = expiration_date_handled
        if reactivate_expired is not None:
            self.reactivate_expired = reactivate_expired
        if restart_sla_expired is not None:
            self.restart_sla_expired = restart_sla_expired
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.owner = owner
        self.accepted_findings = accepted_findings
        if notes is not None:
            self.notes = notes

    @property
    def id(self):
        """Gets the id of this RiskAcceptance.  # noqa: E501


        :return: The id of this RiskAcceptance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RiskAcceptance.


        :param id: The id of this RiskAcceptance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RiskAcceptance.  # noqa: E501

        Descriptive name which in the future may also be used to group risk acceptances together across engagements and products  # noqa: E501

        :return: The name of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RiskAcceptance.

        Descriptive name which in the future may also be used to group risk acceptances together across engagements and products  # noqa: E501

        :param name: The name of this RiskAcceptance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def recommendation(self):
        """Gets the recommendation of this RiskAcceptance.  # noqa: E501

        Recommendation from the security team.  # noqa: E501

        :return: The recommendation of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this RiskAcceptance.

        Recommendation from the security team.  # noqa: E501

        :param recommendation: The recommendation of this RiskAcceptance.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "V", "M", "F", "T"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and recommendation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `recommendation` ({0}), must be one of {1}"  # noqa: E501
                .format(recommendation, allowed_values)
            )

        self._recommendation = recommendation

    @property
    def recommendation_details(self):
        """Gets the recommendation_details of this RiskAcceptance.  # noqa: E501

        Explanation of security recommendation  # noqa: E501

        :return: The recommendation_details of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._recommendation_details

    @recommendation_details.setter
    def recommendation_details(self, recommendation_details):
        """Sets the recommendation_details of this RiskAcceptance.

        Explanation of security recommendation  # noqa: E501

        :param recommendation_details: The recommendation_details of this RiskAcceptance.  # noqa: E501
        :type: str
        """

        self._recommendation_details = recommendation_details

    @property
    def decision(self):
        """Gets the decision of this RiskAcceptance.  # noqa: E501

        Risk treatment decision by risk owner  # noqa: E501

        :return: The decision of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this RiskAcceptance.

        Risk treatment decision by risk owner  # noqa: E501

        :param decision: The decision of this RiskAcceptance.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "V", "M", "F", "T"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and decision not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `decision` ({0}), must be one of {1}"  # noqa: E501
                .format(decision, allowed_values)
            )

        self._decision = decision

    @property
    def decision_details(self):
        """Gets the decision_details of this RiskAcceptance.  # noqa: E501

        If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s).  # noqa: E501

        :return: The decision_details of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._decision_details

    @decision_details.setter
    def decision_details(self, decision_details):
        """Sets the decision_details of this RiskAcceptance.

        If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s).  # noqa: E501

        :param decision_details: The decision_details of this RiskAcceptance.  # noqa: E501
        :type: str
        """

        self._decision_details = decision_details

    @property
    def accepted_by(self):
        """Gets the accepted_by of this RiskAcceptance.  # noqa: E501

        The person that accepts the risk, can be outside of DefectDojo.  # noqa: E501

        :return: The accepted_by of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._accepted_by

    @accepted_by.setter
    def accepted_by(self, accepted_by):
        """Sets the accepted_by of this RiskAcceptance.

        The person that accepts the risk, can be outside of DefectDojo.  # noqa: E501

        :param accepted_by: The accepted_by of this RiskAcceptance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                accepted_by is not None and len(accepted_by) > 200):
            raise ValueError("Invalid value for `accepted_by`, length must be less than or equal to `200`")  # noqa: E501

        self._accepted_by = accepted_by

    @property
    def path(self):
        """Gets the path of this RiskAcceptance.  # noqa: E501


        :return: The path of this RiskAcceptance.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RiskAcceptance.


        :param path: The path of this RiskAcceptance.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def expiration_date(self):
        """Gets the expiration_date of this RiskAcceptance.  # noqa: E501

        When the risk acceptance expires, the findings will be reactivated (unless disabled below).  # noqa: E501

        :return: The expiration_date of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this RiskAcceptance.

        When the risk acceptance expires, the findings will be reactivated (unless disabled below).  # noqa: E501

        :param expiration_date: The expiration_date of this RiskAcceptance.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def expiration_date_warned(self):
        """Gets the expiration_date_warned of this RiskAcceptance.  # noqa: E501

        (readonly) Date at which notice about the risk acceptance expiration was sent.  # noqa: E501

        :return: The expiration_date_warned of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_warned

    @expiration_date_warned.setter
    def expiration_date_warned(self, expiration_date_warned):
        """Sets the expiration_date_warned of this RiskAcceptance.

        (readonly) Date at which notice about the risk acceptance expiration was sent.  # noqa: E501

        :param expiration_date_warned: The expiration_date_warned of this RiskAcceptance.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_warned = expiration_date_warned

    @property
    def expiration_date_handled(self):
        """Gets the expiration_date_handled of this RiskAcceptance.  # noqa: E501

        (readonly) When the risk acceptance expiration was handled (manually or by the daily job).  # noqa: E501

        :return: The expiration_date_handled of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_handled

    @expiration_date_handled.setter
    def expiration_date_handled(self, expiration_date_handled):
        """Sets the expiration_date_handled of this RiskAcceptance.

        (readonly) When the risk acceptance expiration was handled (manually or by the daily job).  # noqa: E501

        :param expiration_date_handled: The expiration_date_handled of this RiskAcceptance.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_handled = expiration_date_handled

    @property
    def reactivate_expired(self):
        """Gets the reactivate_expired of this RiskAcceptance.  # noqa: E501

        Reactivate findings when risk acceptance expires?  # noqa: E501

        :return: The reactivate_expired of this RiskAcceptance.  # noqa: E501
        :rtype: bool
        """
        return self._reactivate_expired

    @reactivate_expired.setter
    def reactivate_expired(self, reactivate_expired):
        """Sets the reactivate_expired of this RiskAcceptance.

        Reactivate findings when risk acceptance expires?  # noqa: E501

        :param reactivate_expired: The reactivate_expired of this RiskAcceptance.  # noqa: E501
        :type: bool
        """

        self._reactivate_expired = reactivate_expired

    @property
    def restart_sla_expired(self):
        """Gets the restart_sla_expired of this RiskAcceptance.  # noqa: E501

        When enabled, the SLA for findings is restarted when the risk acceptance expires.  # noqa: E501

        :return: The restart_sla_expired of this RiskAcceptance.  # noqa: E501
        :rtype: bool
        """
        return self._restart_sla_expired

    @restart_sla_expired.setter
    def restart_sla_expired(self, restart_sla_expired):
        """Sets the restart_sla_expired of this RiskAcceptance.

        When enabled, the SLA for findings is restarted when the risk acceptance expires.  # noqa: E501

        :param restart_sla_expired: The restart_sla_expired of this RiskAcceptance.  # noqa: E501
        :type: bool
        """

        self._restart_sla_expired = restart_sla_expired

    @property
    def created(self):
        """Gets the created of this RiskAcceptance.  # noqa: E501


        :return: The created of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RiskAcceptance.


        :param created: The created of this RiskAcceptance.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this RiskAcceptance.  # noqa: E501


        :return: The updated of this RiskAcceptance.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RiskAcceptance.


        :param updated: The updated of this RiskAcceptance.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def owner(self):
        """Gets the owner of this RiskAcceptance.  # noqa: E501

        User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance.  # noqa: E501

        :return: The owner of this RiskAcceptance.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RiskAcceptance.

        User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk acceptance.  # noqa: E501

        :param owner: The owner of this RiskAcceptance.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def accepted_findings(self):
        """Gets the accepted_findings of this RiskAcceptance.  # noqa: E501


        :return: The accepted_findings of this RiskAcceptance.  # noqa: E501
        :rtype: list[int]
        """
        return self._accepted_findings

    @accepted_findings.setter
    def accepted_findings(self, accepted_findings):
        """Sets the accepted_findings of this RiskAcceptance.


        :param accepted_findings: The accepted_findings of this RiskAcceptance.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and accepted_findings is None:  # noqa: E501
            raise ValueError("Invalid value for `accepted_findings`, must not be `None`")  # noqa: E501

        self._accepted_findings = accepted_findings

    @property
    def notes(self):
        """Gets the notes of this RiskAcceptance.  # noqa: E501


        :return: The notes of this RiskAcceptance.  # noqa: E501
        :rtype: list[int]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this RiskAcceptance.


        :param notes: The notes of this RiskAcceptance.  # noqa: E501
        :type: list[int]
        """

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
        if not isinstance(other, RiskAcceptance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskAcceptance):
            return True

        return self.to_dict() != other.to_dict()
