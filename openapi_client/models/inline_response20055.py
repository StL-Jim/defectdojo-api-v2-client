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


class InlineResponse20055(object):
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
        'phone_number': 'str',
        'cell_number': 'str',
        'twitter_username': 'str',
        'github_username': 'str',
        'slack_username': 'str',
        'slack_user_id': 'str',
        'block_execution': 'bool',
        'force_password_reset': 'bool',
        'user': 'int',
        'prefetch': 'InlineResponse20054Prefetch'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'phone_number': 'phone_number',
        'cell_number': 'cell_number',
        'twitter_username': 'twitter_username',
        'github_username': 'github_username',
        'slack_username': 'slack_username',
        'slack_user_id': 'slack_user_id',
        'block_execution': 'block_execution',
        'force_password_reset': 'force_password_reset',
        'user': 'user',
        'prefetch': 'prefetch'
    }

    def __init__(self, id=None, title=None, phone_number=None, cell_number=None, twitter_username=None, github_username=None, slack_username=None, slack_user_id=None, block_execution=None, force_password_reset=None, user=None, prefetch=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20055 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._phone_number = None
        self._cell_number = None
        self._twitter_username = None
        self._github_username = None
        self._slack_username = None
        self._slack_user_id = None
        self._block_execution = None
        self._force_password_reset = None
        self._user = None
        self._prefetch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.title = title
        if phone_number is not None:
            self.phone_number = phone_number
        if cell_number is not None:
            self.cell_number = cell_number
        self.twitter_username = twitter_username
        self.github_username = github_username
        self.slack_username = slack_username
        self.slack_user_id = slack_user_id
        if block_execution is not None:
            self.block_execution = block_execution
        if force_password_reset is not None:
            self.force_password_reset = force_password_reset
        self.user = user
        if prefetch is not None:
            self.prefetch = prefetch

    @property
    def id(self):
        """Gets the id of this InlineResponse20055.  # noqa: E501


        :return: The id of this InlineResponse20055.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20055.


        :param id: The id of this InlineResponse20055.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this InlineResponse20055.  # noqa: E501


        :return: The title of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse20055.


        :param title: The title of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 150):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `150`")  # noqa: E501

        self._title = title

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse20055.  # noqa: E501

        Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.  # noqa: E501

        :return: The phone_number of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse20055.

        Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone_number is not None and len(phone_number) > 15):
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                phone_number is not None and not re.search(r'^\+?1?\d{9,15}$', phone_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `phone_number`, must be a follow pattern or equal to `/^\+?1?\d{9,15}$/`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def cell_number(self):
        """Gets the cell_number of this InlineResponse20055.  # noqa: E501

        Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.  # noqa: E501

        :return: The cell_number of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._cell_number

    @cell_number.setter
    def cell_number(self, cell_number):
        """Sets the cell_number of this InlineResponse20055.

        Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.  # noqa: E501

        :param cell_number: The cell_number of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cell_number is not None and len(cell_number) > 15):
            raise ValueError("Invalid value for `cell_number`, length must be less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cell_number is not None and not re.search(r'^\+?1?\d{9,15}$', cell_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `cell_number`, must be a follow pattern or equal to `/^\+?1?\d{9,15}$/`")  # noqa: E501

        self._cell_number = cell_number

    @property
    def twitter_username(self):
        """Gets the twitter_username of this InlineResponse20055.  # noqa: E501


        :return: The twitter_username of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._twitter_username

    @twitter_username.setter
    def twitter_username(self, twitter_username):
        """Sets the twitter_username of this InlineResponse20055.


        :param twitter_username: The twitter_username of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                twitter_username is not None and len(twitter_username) > 150):
            raise ValueError("Invalid value for `twitter_username`, length must be less than or equal to `150`")  # noqa: E501

        self._twitter_username = twitter_username

    @property
    def github_username(self):
        """Gets the github_username of this InlineResponse20055.  # noqa: E501


        :return: The github_username of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._github_username

    @github_username.setter
    def github_username(self, github_username):
        """Sets the github_username of this InlineResponse20055.


        :param github_username: The github_username of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                github_username is not None and len(github_username) > 150):
            raise ValueError("Invalid value for `github_username`, length must be less than or equal to `150`")  # noqa: E501

        self._github_username = github_username

    @property
    def slack_username(self):
        """Gets the slack_username of this InlineResponse20055.  # noqa: E501

        Email address associated with your slack account  # noqa: E501

        :return: The slack_username of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._slack_username

    @slack_username.setter
    def slack_username(self, slack_username):
        """Sets the slack_username of this InlineResponse20055.

        Email address associated with your slack account  # noqa: E501

        :param slack_username: The slack_username of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slack_username is not None and len(slack_username) > 150):
            raise ValueError("Invalid value for `slack_username`, length must be less than or equal to `150`")  # noqa: E501

        self._slack_username = slack_username

    @property
    def slack_user_id(self):
        """Gets the slack_user_id of this InlineResponse20055.  # noqa: E501


        :return: The slack_user_id of this InlineResponse20055.  # noqa: E501
        :rtype: str
        """
        return self._slack_user_id

    @slack_user_id.setter
    def slack_user_id(self, slack_user_id):
        """Sets the slack_user_id of this InlineResponse20055.


        :param slack_user_id: The slack_user_id of this InlineResponse20055.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slack_user_id is not None and len(slack_user_id) > 25):
            raise ValueError("Invalid value for `slack_user_id`, length must be less than or equal to `25`")  # noqa: E501

        self._slack_user_id = slack_user_id

    @property
    def block_execution(self):
        """Gets the block_execution of this InlineResponse20055.  # noqa: E501

        Instead of async deduping a finding the findings will be deduped synchronously and will 'block' the user until completion.  # noqa: E501

        :return: The block_execution of this InlineResponse20055.  # noqa: E501
        :rtype: bool
        """
        return self._block_execution

    @block_execution.setter
    def block_execution(self, block_execution):
        """Sets the block_execution of this InlineResponse20055.

        Instead of async deduping a finding the findings will be deduped synchronously and will 'block' the user until completion.  # noqa: E501

        :param block_execution: The block_execution of this InlineResponse20055.  # noqa: E501
        :type: bool
        """

        self._block_execution = block_execution

    @property
    def force_password_reset(self):
        """Gets the force_password_reset of this InlineResponse20055.  # noqa: E501

        Forces this user to reset their password on next login.  # noqa: E501

        :return: The force_password_reset of this InlineResponse20055.  # noqa: E501
        :rtype: bool
        """
        return self._force_password_reset

    @force_password_reset.setter
    def force_password_reset(self, force_password_reset):
        """Sets the force_password_reset of this InlineResponse20055.

        Forces this user to reset their password on next login.  # noqa: E501

        :param force_password_reset: The force_password_reset of this InlineResponse20055.  # noqa: E501
        :type: bool
        """

        self._force_password_reset = force_password_reset

    @property
    def user(self):
        """Gets the user of this InlineResponse20055.  # noqa: E501


        :return: The user of this InlineResponse20055.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineResponse20055.


        :param user: The user of this InlineResponse20055.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def prefetch(self):
        """Gets the prefetch of this InlineResponse20055.  # noqa: E501


        :return: The prefetch of this InlineResponse20055.  # noqa: E501
        :rtype: InlineResponse20054Prefetch
        """
        return self._prefetch

    @prefetch.setter
    def prefetch(self, prefetch):
        """Sets the prefetch of this InlineResponse20055.


        :param prefetch: The prefetch of this InlineResponse20055.  # noqa: E501
        :type: InlineResponse20054Prefetch
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
        if not isinstance(other, InlineResponse20055):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20055):
            return True

        return self.to_dict() != other.to_dict()
