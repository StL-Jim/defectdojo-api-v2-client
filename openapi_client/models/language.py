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


class Language(object):
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
        'files': 'int',
        'blank': 'int',
        'comment': 'int',
        'code': 'int',
        'created': 'datetime',
        'language': 'int',
        'product': 'int',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'files': 'files',
        'blank': 'blank',
        'comment': 'comment',
        'code': 'code',
        'created': 'created',
        'language': 'language',
        'product': 'product',
        'user': 'user'
    }

    def __init__(self, id=None, files=None, blank=None, comment=None, code=None, created=None, language=None, product=None, user=None, local_vars_configuration=None):  # noqa: E501
        """Language - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._files = None
        self._blank = None
        self._comment = None
        self._code = None
        self._created = None
        self._language = None
        self._product = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.files = files
        self.blank = blank
        self.comment = comment
        self.code = code
        if created is not None:
            self.created = created
        self.language = language
        self.product = product
        self.user = user

    @property
    def id(self):
        """Gets the id of this Language.  # noqa: E501


        :return: The id of this Language.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Language.


        :param id: The id of this Language.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def files(self):
        """Gets the files of this Language.  # noqa: E501


        :return: The files of this Language.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Language.


        :param files: The files of this Language.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                files is not None and files > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `files`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                files is not None and files < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `files`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._files = files

    @property
    def blank(self):
        """Gets the blank of this Language.  # noqa: E501


        :return: The blank of this Language.  # noqa: E501
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """Sets the blank of this Language.


        :param blank: The blank of this Language.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                blank is not None and blank > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `blank`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                blank is not None and blank < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `blank`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._blank = blank

    @property
    def comment(self):
        """Gets the comment of this Language.  # noqa: E501


        :return: The comment of this Language.  # noqa: E501
        :rtype: int
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Language.


        :param comment: The comment of this Language.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                comment is not None and comment > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `comment`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                comment is not None and comment < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `comment`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._comment = comment

    @property
    def code(self):
        """Gets the code of this Language.  # noqa: E501


        :return: The code of this Language.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Language.


        :param code: The code of this Language.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and code > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `code`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and code < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `code`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._code = code

    @property
    def created(self):
        """Gets the created of this Language.  # noqa: E501


        :return: The created of this Language.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Language.


        :param created: The created of this Language.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def language(self):
        """Gets the language of this Language.  # noqa: E501


        :return: The language of this Language.  # noqa: E501
        :rtype: int
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Language.


        :param language: The language of this Language.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def product(self):
        """Gets the product of this Language.  # noqa: E501


        :return: The product of this Language.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Language.


        :param product: The product of this Language.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def user(self):
        """Gets the user of this Language.  # noqa: E501


        :return: The user of this Language.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Language.


        :param user: The user of this Language.  # noqa: E501
        :type: int
        """

        self._user = user

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
        if not isinstance(other, Language):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Language):
            return True

        return self.to_dict() != other.to_dict()
