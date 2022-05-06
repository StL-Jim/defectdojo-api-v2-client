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


class Endpoint(object):
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
        'tags': 'list[str]',
        'protocol': 'str',
        'userinfo': 'str',
        'host': 'str',
        'port': 'int',
        'path': 'str',
        'query': 'str',
        'fragment': 'str',
        'product': 'int',
        'endpoint_params': 'list[int]',
        'endpoint_status': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'tags': 'tags',
        'protocol': 'protocol',
        'userinfo': 'userinfo',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'query': 'query',
        'fragment': 'fragment',
        'product': 'product',
        'endpoint_params': 'endpoint_params',
        'endpoint_status': 'endpoint_status'
    }

    def __init__(self, id=None, tags=None, protocol=None, userinfo=None, host=None, port=None, path=None, query=None, fragment=None, product=None, endpoint_params=None, endpoint_status=None, local_vars_configuration=None):  # noqa: E501
        """Endpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._tags = None
        self._protocol = None
        self._userinfo = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None
        self._fragment = None
        self._product = None
        self._endpoint_params = None
        self._endpoint_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags
        self.protocol = protocol
        self.userinfo = userinfo
        self.host = host
        self.port = port
        self.path = path
        self.query = query
        self.fragment = fragment
        self.product = product
        if endpoint_params is not None:
            self.endpoint_params = endpoint_params
        if endpoint_status is not None:
            self.endpoint_status = endpoint_status

    @property
    def id(self):
        """Gets the id of this Endpoint.  # noqa: E501


        :return: The id of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Endpoint.


        :param id: The id of this Endpoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tags(self):
        """Gets the tags of this Endpoint.  # noqa: E501


        :return: The tags of this Endpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Endpoint.


        :param tags: The tags of this Endpoint.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def protocol(self):
        """Gets the protocol of this Endpoint.  # noqa: E501

        The communication protocol/scheme such as 'http', 'ftp', 'dns', etc.  # noqa: E501

        :return: The protocol of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Endpoint.

        The communication protocol/scheme such as 'http', 'ftp', 'dns', etc.  # noqa: E501

        :param protocol: The protocol of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                protocol is not None and len(protocol) > 20):
            raise ValueError("Invalid value for `protocol`, length must be less than or equal to `20`")  # noqa: E501

        self._protocol = protocol

    @property
    def userinfo(self):
        """Gets the userinfo of this Endpoint.  # noqa: E501

        User info as 'alice', 'bob', etc.  # noqa: E501

        :return: The userinfo of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._userinfo

    @userinfo.setter
    def userinfo(self, userinfo):
        """Sets the userinfo of this Endpoint.

        User info as 'alice', 'bob', etc.  # noqa: E501

        :param userinfo: The userinfo of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                userinfo is not None and len(userinfo) > 500):
            raise ValueError("Invalid value for `userinfo`, length must be less than or equal to `500`")  # noqa: E501

        self._userinfo = userinfo

    @property
    def host(self):
        """Gets the host of this Endpoint.  # noqa: E501

        The host name or IP address. It must not include the port number. For example '127.0.0.1', 'localhost', 'yourdomain.com'.  # noqa: E501

        :return: The host of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Endpoint.

        The host name or IP address. It must not include the port number. For example '127.0.0.1', 'localhost', 'yourdomain.com'.  # noqa: E501

        :param host: The host of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                host is not None and len(host) > 500):
            raise ValueError("Invalid value for `host`, length must be less than or equal to `500`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this Endpoint.  # noqa: E501

        The network port associated with the endpoint.  # noqa: E501

        :return: The port of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Endpoint.

        The network port associated with the endpoint.  # noqa: E501

        :param port: The port of this Endpoint.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._port = port

    @property
    def path(self):
        """Gets the path of this Endpoint.  # noqa: E501

        The location of the resource, it must not start with a '/'. For example endpoint/420/edit  # noqa: E501

        :return: The path of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Endpoint.

        The location of the resource, it must not start with a '/'. For example endpoint/420/edit  # noqa: E501

        :param path: The path of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) > 500):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `500`")  # noqa: E501

        self._path = path

    @property
    def query(self):
        """Gets the query of this Endpoint.  # noqa: E501

        The query string, the question mark should be omitted.For example 'group=4&team=8'  # noqa: E501

        :return: The query of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Endpoint.

        The query string, the question mark should be omitted.For example 'group=4&team=8'  # noqa: E501

        :param query: The query of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                query is not None and len(query) > 1000):
            raise ValueError("Invalid value for `query`, length must be less than or equal to `1000`")  # noqa: E501

        self._query = query

    @property
    def fragment(self):
        """Gets the fragment of this Endpoint.  # noqa: E501

        The fragment identifier which follows the hash mark. The hash mark should be omitted. For example 'section-13', 'paragraph-2'.  # noqa: E501

        :return: The fragment of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        """Sets the fragment of this Endpoint.

        The fragment identifier which follows the hash mark. The hash mark should be omitted. For example 'section-13', 'paragraph-2'.  # noqa: E501

        :param fragment: The fragment of this Endpoint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fragment is not None and len(fragment) > 500):
            raise ValueError("Invalid value for `fragment`, length must be less than or equal to `500`")  # noqa: E501

        self._fragment = fragment

    @property
    def product(self):
        """Gets the product of this Endpoint.  # noqa: E501


        :return: The product of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Endpoint.


        :param product: The product of this Endpoint.  # noqa: E501
        :type: int
        """

        self._product = product

    @property
    def endpoint_params(self):
        """Gets the endpoint_params of this Endpoint.  # noqa: E501


        :return: The endpoint_params of this Endpoint.  # noqa: E501
        :rtype: list[int]
        """
        return self._endpoint_params

    @endpoint_params.setter
    def endpoint_params(self, endpoint_params):
        """Sets the endpoint_params of this Endpoint.


        :param endpoint_params: The endpoint_params of this Endpoint.  # noqa: E501
        :type: list[int]
        """

        self._endpoint_params = endpoint_params

    @property
    def endpoint_status(self):
        """Gets the endpoint_status of this Endpoint.  # noqa: E501


        :return: The endpoint_status of this Endpoint.  # noqa: E501
        :rtype: list[int]
        """
        return self._endpoint_status

    @endpoint_status.setter
    def endpoint_status(self, endpoint_status):
        """Sets the endpoint_status of this Endpoint.


        :param endpoint_status: The endpoint_status of this Endpoint.  # noqa: E501
        :type: list[int]
        """

        self._endpoint_status = endpoint_status

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
        if not isinstance(other, Endpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Endpoint):
            return True

        return self.to_dict() != other.to_dict()
