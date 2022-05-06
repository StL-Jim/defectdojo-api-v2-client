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


class TestImport(object):
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
        'test_import_finding_action_set': 'list[TestImportFindingAction]',
        'created': 'datetime',
        'modified': 'datetime',
        'import_settings': 'object',
        'type': 'str',
        'version': 'str',
        'build_id': 'str',
        'commit_hash': 'str',
        'branch_tag': 'str',
        'test': 'int',
        'findings_affected': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'test_import_finding_action_set': 'test_import_finding_action_set',
        'created': 'created',
        'modified': 'modified',
        'import_settings': 'import_settings',
        'type': 'type',
        'version': 'version',
        'build_id': 'build_id',
        'commit_hash': 'commit_hash',
        'branch_tag': 'branch_tag',
        'test': 'test',
        'findings_affected': 'findings_affected'
    }

    def __init__(self, id=None, test_import_finding_action_set=None, created=None, modified=None, import_settings=None, type=None, version=None, build_id=None, commit_hash=None, branch_tag=None, test=None, findings_affected=None, local_vars_configuration=None):  # noqa: E501
        """TestImport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._test_import_finding_action_set = None
        self._created = None
        self._modified = None
        self._import_settings = None
        self._type = None
        self._version = None
        self._build_id = None
        self._commit_hash = None
        self._branch_tag = None
        self._test = None
        self._findings_affected = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if test_import_finding_action_set is not None:
            self.test_import_finding_action_set = test_import_finding_action_set
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        self.import_settings = import_settings
        if type is not None:
            self.type = type
        self.version = version
        self.build_id = build_id
        self.commit_hash = commit_hash
        self.branch_tag = branch_tag
        if test is not None:
            self.test = test
        if findings_affected is not None:
            self.findings_affected = findings_affected

    @property
    def id(self):
        """Gets the id of this TestImport.  # noqa: E501


        :return: The id of this TestImport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestImport.


        :param id: The id of this TestImport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def test_import_finding_action_set(self):
        """Gets the test_import_finding_action_set of this TestImport.  # noqa: E501


        :return: The test_import_finding_action_set of this TestImport.  # noqa: E501
        :rtype: list[TestImportFindingAction]
        """
        return self._test_import_finding_action_set

    @test_import_finding_action_set.setter
    def test_import_finding_action_set(self, test_import_finding_action_set):
        """Sets the test_import_finding_action_set of this TestImport.


        :param test_import_finding_action_set: The test_import_finding_action_set of this TestImport.  # noqa: E501
        :type: list[TestImportFindingAction]
        """

        self._test_import_finding_action_set = test_import_finding_action_set

    @property
    def created(self):
        """Gets the created of this TestImport.  # noqa: E501


        :return: The created of this TestImport.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TestImport.


        :param created: The created of this TestImport.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this TestImport.  # noqa: E501


        :return: The modified of this TestImport.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this TestImport.


        :param modified: The modified of this TestImport.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def import_settings(self):
        """Gets the import_settings of this TestImport.  # noqa: E501


        :return: The import_settings of this TestImport.  # noqa: E501
        :rtype: object
        """
        return self._import_settings

    @import_settings.setter
    def import_settings(self, import_settings):
        """Sets the import_settings of this TestImport.


        :param import_settings: The import_settings of this TestImport.  # noqa: E501
        :type: object
        """

        self._import_settings = import_settings

    @property
    def type(self):
        """Gets the type of this TestImport.  # noqa: E501


        :return: The type of this TestImport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TestImport.


        :param type: The type of this TestImport.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 64):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def version(self):
        """Gets the version of this TestImport.  # noqa: E501


        :return: The version of this TestImport.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TestImport.


        :param version: The version of this TestImport.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 100):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `100`")  # noqa: E501

        self._version = version

    @property
    def build_id(self):
        """Gets the build_id of this TestImport.  # noqa: E501

        Build ID that was tested, a reimport may update this field.  # noqa: E501

        :return: The build_id of this TestImport.  # noqa: E501
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this TestImport.

        Build ID that was tested, a reimport may update this field.  # noqa: E501

        :param build_id: The build_id of this TestImport.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                build_id is not None and len(build_id) > 150):
            raise ValueError("Invalid value for `build_id`, length must be less than or equal to `150`")  # noqa: E501

        self._build_id = build_id

    @property
    def commit_hash(self):
        """Gets the commit_hash of this TestImport.  # noqa: E501

        Commit hash tested, a reimport may update this field.  # noqa: E501

        :return: The commit_hash of this TestImport.  # noqa: E501
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this TestImport.

        Commit hash tested, a reimport may update this field.  # noqa: E501

        :param commit_hash: The commit_hash of this TestImport.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit_hash is not None and len(commit_hash) > 150):
            raise ValueError("Invalid value for `commit_hash`, length must be less than or equal to `150`")  # noqa: E501

        self._commit_hash = commit_hash

    @property
    def branch_tag(self):
        """Gets the branch_tag of this TestImport.  # noqa: E501

        Tag or branch that was tested, a reimport may update this field.  # noqa: E501

        :return: The branch_tag of this TestImport.  # noqa: E501
        :rtype: str
        """
        return self._branch_tag

    @branch_tag.setter
    def branch_tag(self, branch_tag):
        """Sets the branch_tag of this TestImport.

        Tag or branch that was tested, a reimport may update this field.  # noqa: E501

        :param branch_tag: The branch_tag of this TestImport.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                branch_tag is not None and len(branch_tag) > 150):
            raise ValueError("Invalid value for `branch_tag`, length must be less than or equal to `150`")  # noqa: E501

        self._branch_tag = branch_tag

    @property
    def test(self):
        """Gets the test of this TestImport.  # noqa: E501


        :return: The test of this TestImport.  # noqa: E501
        :rtype: int
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this TestImport.


        :param test: The test of this TestImport.  # noqa: E501
        :type: int
        """

        self._test = test

    @property
    def findings_affected(self):
        """Gets the findings_affected of this TestImport.  # noqa: E501


        :return: The findings_affected of this TestImport.  # noqa: E501
        :rtype: list[int]
        """
        return self._findings_affected

    @findings_affected.setter
    def findings_affected(self, findings_affected):
        """Sets the findings_affected of this TestImport.


        :param findings_affected: The findings_affected of this TestImport.  # noqa: E501
        :type: list[int]
        """

        self._findings_affected = findings_affected

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
        if not isinstance(other, TestImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestImport):
            return True

        return self.to_dict() != other.to_dict()
