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


class ParcelAccount(object):
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
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'carrier': 'str',
        'account_no': 'str',
        'client': 'int',
        'name': 'str',
        'manifest_partner_id': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'carrier': 'carrier',
        'account_no': 'accountNo',
        'client': 'client',
        'name': 'name',
        'manifest_partner_id': 'manifestPartnerId',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, carrier=None, account_no=None, client=None, name=None, manifest_partner_id=None, custom_fields=None):  # noqa: E501
        """ParcelAccount - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._carrier = None
        self._account_no = None
        self._client = None
        self._name = None
        self._manifest_partner_id = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.carrier = carrier
        self.account_no = account_no
        if client is not None:
            self.client = client
        self.name = name
        self.manifest_partner_id = manifest_partner_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ParcelAccount.  # noqa: E501


        :return: The id of this ParcelAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParcelAccount.


        :param id: The id of this ParcelAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ParcelAccount.  # noqa: E501


        :return: The create_date of this ParcelAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ParcelAccount.


        :param create_date: The create_date of this ParcelAccount.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ParcelAccount.  # noqa: E501


        :return: The modify_date of this ParcelAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ParcelAccount.


        :param modify_date: The modify_date of this ParcelAccount.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def carrier(self):
        """Gets the carrier of this ParcelAccount.  # noqa: E501


        :return: The carrier of this ParcelAccount.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this ParcelAccount.


        :param carrier: The carrier of this ParcelAccount.  # noqa: E501
        :type: str
        """
        if carrier is None:
            raise ValueError("Invalid value for `carrier`, must not be `None`")  # noqa: E501

        self._carrier = carrier

    @property
    def account_no(self):
        """Gets the account_no of this ParcelAccount.  # noqa: E501


        :return: The account_no of this ParcelAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this ParcelAccount.


        :param account_no: The account_no of this ParcelAccount.  # noqa: E501
        :type: str
        """
        if account_no is None:
            raise ValueError("Invalid value for `account_no`, must not be `None`")  # noqa: E501

        self._account_no = account_no

    @property
    def client(self):
        """Gets the client of this ParcelAccount.  # noqa: E501


        :return: The client of this ParcelAccount.  # noqa: E501
        :rtype: int
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ParcelAccount.


        :param client: The client of this ParcelAccount.  # noqa: E501
        :type: int
        """

        self._client = client

    @property
    def name(self):
        """Gets the name of this ParcelAccount.  # noqa: E501


        :return: The name of this ParcelAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParcelAccount.


        :param name: The name of this ParcelAccount.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def manifest_partner_id(self):
        """Gets the manifest_partner_id of this ParcelAccount.  # noqa: E501


        :return: The manifest_partner_id of this ParcelAccount.  # noqa: E501
        :rtype: str
        """
        return self._manifest_partner_id

    @manifest_partner_id.setter
    def manifest_partner_id(self, manifest_partner_id):
        """Sets the manifest_partner_id of this ParcelAccount.


        :param manifest_partner_id: The manifest_partner_id of this ParcelAccount.  # noqa: E501
        :type: str
        """
        if manifest_partner_id is None:
            raise ValueError("Invalid value for `manifest_partner_id`, must not be `None`")  # noqa: E501

        self._manifest_partner_id = manifest_partner_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ParcelAccount.  # noqa: E501


        :return: The custom_fields of this ParcelAccount.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ParcelAccount.


        :param custom_fields: The custom_fields of this ParcelAccount.  # noqa: E501
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
        if not isinstance(other, ParcelAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other