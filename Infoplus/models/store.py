# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Store(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'store_name': 'str',
        'store_id': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'store_name': 'storeName',
        'store_id': 'storeId',
        'custom_fields': 'customFields'
    }

    def __init__(self, store_name=None, store_id=None, custom_fields=None):  # noqa: E501
        """Store - a model defined in Swagger"""  # noqa: E501

        self._store_name = None
        self._store_id = None
        self._custom_fields = None
        self.discriminator = None

        self.store_name = store_name
        self.store_id = store_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def store_name(self):
        """Gets the store_name of this Store.  # noqa: E501


        :return: The store_name of this Store.  # noqa: E501
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        """Sets the store_name of this Store.


        :param store_name: The store_name of this Store.  # noqa: E501
        :type: str
        """
        if store_name is None:
            raise ValueError("Invalid value for `store_name`, must not be `None`")  # noqa: E501

        self._store_name = store_name

    @property
    def store_id(self):
        """Gets the store_id of this Store.  # noqa: E501


        :return: The store_id of this Store.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this Store.


        :param store_id: The store_id of this Store.  # noqa: E501
        :type: str
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")  # noqa: E501

        self._store_id = store_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Store.  # noqa: E501


        :return: The custom_fields of this Store.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Store.


        :param custom_fields: The custom_fields of this Store.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, Store):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other