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


class Note(object):
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
        'author': 'UserStub',
        'editor': 'UserStub',
        'history': 'list[NoteHistory]',
        'entry': 'str',
        'date': 'datetime',
        'private': 'bool',
        'edited': 'bool',
        'edit_time': 'datetime',
        'note_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'author': 'author',
        'editor': 'editor',
        'history': 'history',
        'entry': 'entry',
        'date': 'date',
        'private': 'private',
        'edited': 'edited',
        'edit_time': 'edit_time',
        'note_type': 'note_type'
    }

    def __init__(self, id=None, author=None, editor=None, history=None, entry=None, date=None, private=None, edited=None, edit_time=None, note_type=None, local_vars_configuration=None):  # noqa: E501
        """Note - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._author = None
        self._editor = None
        self._history = None
        self._entry = None
        self._date = None
        self._private = None
        self._edited = None
        self._edit_time = None
        self._note_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if author is not None:
            self.author = author
        if editor is not None:
            self.editor = editor
        if history is not None:
            self.history = history
        self.entry = entry
        if date is not None:
            self.date = date
        if private is not None:
            self.private = private
        if edited is not None:
            self.edited = edited
        if edit_time is not None:
            self.edit_time = edit_time
        self.note_type = note_type

    @property
    def id(self):
        """Gets the id of this Note.  # noqa: E501


        :return: The id of this Note.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Note.


        :param id: The id of this Note.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def author(self):
        """Gets the author of this Note.  # noqa: E501


        :return: The author of this Note.  # noqa: E501
        :rtype: UserStub
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Note.


        :param author: The author of this Note.  # noqa: E501
        :type: UserStub
        """

        self._author = author

    @property
    def editor(self):
        """Gets the editor of this Note.  # noqa: E501


        :return: The editor of this Note.  # noqa: E501
        :rtype: UserStub
        """
        return self._editor

    @editor.setter
    def editor(self, editor):
        """Sets the editor of this Note.


        :param editor: The editor of this Note.  # noqa: E501
        :type: UserStub
        """

        self._editor = editor

    @property
    def history(self):
        """Gets the history of this Note.  # noqa: E501


        :return: The history of this Note.  # noqa: E501
        :rtype: list[NoteHistory]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this Note.


        :param history: The history of this Note.  # noqa: E501
        :type: list[NoteHistory]
        """

        self._history = history

    @property
    def entry(self):
        """Gets the entry of this Note.  # noqa: E501


        :return: The entry of this Note.  # noqa: E501
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this Note.


        :param entry: The entry of this Note.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entry is None:  # noqa: E501
            raise ValueError("Invalid value for `entry`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entry is not None and len(entry) < 1):
            raise ValueError("Invalid value for `entry`, length must be greater than or equal to `1`")  # noqa: E501

        self._entry = entry

    @property
    def date(self):
        """Gets the date of this Note.  # noqa: E501


        :return: The date of this Note.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Note.


        :param date: The date of this Note.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def private(self):
        """Gets the private of this Note.  # noqa: E501


        :return: The private of this Note.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Note.


        :param private: The private of this Note.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def edited(self):
        """Gets the edited of this Note.  # noqa: E501


        :return: The edited of this Note.  # noqa: E501
        :rtype: bool
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """Sets the edited of this Note.


        :param edited: The edited of this Note.  # noqa: E501
        :type: bool
        """

        self._edited = edited

    @property
    def edit_time(self):
        """Gets the edit_time of this Note.  # noqa: E501


        :return: The edit_time of this Note.  # noqa: E501
        :rtype: datetime
        """
        return self._edit_time

    @edit_time.setter
    def edit_time(self, edit_time):
        """Sets the edit_time of this Note.


        :param edit_time: The edit_time of this Note.  # noqa: E501
        :type: datetime
        """

        self._edit_time = edit_time

    @property
    def note_type(self):
        """Gets the note_type of this Note.  # noqa: E501


        :return: The note_type of this Note.  # noqa: E501
        :rtype: int
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        """Sets the note_type of this Note.


        :param note_type: The note_type of this Note.  # noqa: E501
        :type: int
        """

        self._note_type = note_type

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
        if not isinstance(other, Note):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Note):
            return True

        return self.to_dict() != other.to_dict()
