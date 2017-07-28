# coding: utf-8

"""
ItemReceiptApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ItemReceiptApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_item_receipt_audit(self, item_receipt_id, item_receipt_audit, **kwargs):
        """
        Add new audit for an itemReceipt
        Adds an audit to an existing itemReceipt.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_item_receipt_audit(item_receipt_id, item_receipt_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to add an audit to (required)
        :param str item_receipt_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id', 'item_receipt_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_item_receipt_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `add_item_receipt_audit`")
        # verify the required parameter 'item_receipt_audit' is set
        if ('item_receipt_audit' not in params) or (params['item_receipt_audit'] is None):
            raise ValueError("Missing the required parameter `item_receipt_audit` when calling `add_item_receipt_audit`")

        resource_path = '/beta/itemReceipt/{itemReceiptId}/audit/{itemReceiptAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']
        if 'item_receipt_audit' in params:
            path_params['itemReceiptAudit'] = params['item_receipt_audit']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_item_receipt_tag(self, item_receipt_id, item_receipt_tag, **kwargs):
        """
        Add new tags for an itemReceipt.
        Adds a tag to an existing itemReceipt.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_item_receipt_tag(item_receipt_id, item_receipt_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to add a tag to (required)
        :param str item_receipt_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id', 'item_receipt_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_item_receipt_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `add_item_receipt_tag`")
        # verify the required parameter 'item_receipt_tag' is set
        if ('item_receipt_tag' not in params) or (params['item_receipt_tag'] is None):
            raise ValueError("Missing the required parameter `item_receipt_tag` when calling `add_item_receipt_tag`")

        resource_path = '/beta/itemReceipt/{itemReceiptId}/tag/{itemReceiptTag}'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']
        if 'item_receipt_tag' in params:
            path_params['itemReceiptTag'] = params['item_receipt_tag']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_item_receipt_tag(self, item_receipt_id, item_receipt_tag, **kwargs):
        """
        Delete a tag for an itemReceipt.
        Deletes an existing itemReceipt tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_item_receipt_tag(item_receipt_id, item_receipt_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to remove tag from (required)
        :param str item_receipt_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id', 'item_receipt_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_receipt_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `delete_item_receipt_tag`")
        # verify the required parameter 'item_receipt_tag' is set
        if ('item_receipt_tag' not in params) or (params['item_receipt_tag'] is None):
            raise ValueError("Missing the required parameter `item_receipt_tag` when calling `delete_item_receipt_tag`")

        resource_path = '/beta/itemReceipt/{itemReceiptId}/tag/{itemReceiptTag}'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']
        if 'item_receipt_tag' in params:
            path_params['itemReceiptTag'] = params['item_receipt_tag']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_duplicate_item_receipt_by_id(self, item_receipt_id, **kwargs):
        """
        Get a duplicated an itemReceipt by id
        Returns a duplicated itemReceipt identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_item_receipt_by_id(item_receipt_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to be duplicated. (required)
        :return: ItemReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_item_receipt_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `get_duplicate_item_receipt_by_id`")

        resource_path = '/beta/itemReceipt/duplicate/{itemReceiptId}'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ItemReceipt',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_item_receipt_by_filter(self, **kwargs):
        """
        Search itemReceipts by filter
        Returns the list of itemReceipts that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_item_receipt_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[ItemReceipt]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page', 'limit', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_receipt_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/itemReceipt/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ItemReceipt]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_item_receipt_by_id(self, item_receipt_id, **kwargs):
        """
        Get an itemReceipt by id
        Returns the itemReceipt identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_item_receipt_by_id(item_receipt_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to be returned. (required)
        :return: ItemReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_receipt_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `get_item_receipt_by_id`")

        resource_path = '/beta/itemReceipt/{itemReceiptId}'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ItemReceipt',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_item_receipt_tags(self, item_receipt_id, **kwargs):
        """
        Get the tags for an itemReceipt.
        Get all existing itemReceipt tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_item_receipt_tags(item_receipt_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int item_receipt_id: Id of the itemReceipt to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_receipt_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_receipt_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_receipt_id' is set
        if ('item_receipt_id' not in params) or (params['item_receipt_id'] is None):
            raise ValueError("Missing the required parameter `item_receipt_id` when calling `get_item_receipt_tags`")

        resource_path = '/beta/itemReceipt/{itemReceiptId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'item_receipt_id' in params:
            path_params['itemReceiptId'] = params['item_receipt_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_item_receipt(self, body, **kwargs):
        """
        Update an itemReceipt
        Updates an existing itemReceipt using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_item_receipt(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ItemReceipt body: ItemReceipt to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_item_receipt" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_item_receipt`")

        resource_path = '/beta/itemReceipt'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_item_receipt_custom_fields(self, body, **kwargs):
        """
        Update an itemReceipt custom fields
        Updates an existing itemReceipt custom fields using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_item_receipt_custom_fields(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ItemReceipt body: ItemReceipt to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_item_receipt_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_item_receipt_custom_fields`")

        resource_path = '/beta/itemReceipt/customFields'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
