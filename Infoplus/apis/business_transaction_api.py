# coding: utf-8

"""
BusinessTransactionApi.py
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


class BusinessTransactionApi(object):
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

    def add_business_transaction_audit(self, business_transaction_id, business_transaction_audit, **kwargs):
        """
        Add new audit for a businessTransaction
        Adds an audit to an existing businessTransaction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_business_transaction_audit(business_transaction_id, business_transaction_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to add an audit to (required)
        :param str business_transaction_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id', 'business_transaction_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_business_transaction_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `add_business_transaction_audit`")
        # verify the required parameter 'business_transaction_audit' is set
        if ('business_transaction_audit' not in params) or (params['business_transaction_audit'] is None):
            raise ValueError("Missing the required parameter `business_transaction_audit` when calling `add_business_transaction_audit`")

        resource_path = '/beta/businessTransaction/{businessTransactionId}/audit/{businessTransactionAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']
        if 'business_transaction_audit' in params:
            path_params['businessTransactionAudit'] = params['business_transaction_audit']

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

    def add_business_transaction_tag(self, business_transaction_id, business_transaction_tag, **kwargs):
        """
        Add new tags for a businessTransaction.
        Adds a tag to an existing businessTransaction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_business_transaction_tag(business_transaction_id, business_transaction_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to add a tag to (required)
        :param str business_transaction_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id', 'business_transaction_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_business_transaction_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `add_business_transaction_tag`")
        # verify the required parameter 'business_transaction_tag' is set
        if ('business_transaction_tag' not in params) or (params['business_transaction_tag'] is None):
            raise ValueError("Missing the required parameter `business_transaction_tag` when calling `add_business_transaction_tag`")

        resource_path = '/beta/businessTransaction/{businessTransactionId}/tag/{businessTransactionTag}'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']
        if 'business_transaction_tag' in params:
            path_params['businessTransactionTag'] = params['business_transaction_tag']

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

    def delete_business_transaction_tag(self, business_transaction_id, business_transaction_tag, **kwargs):
        """
        Delete a tag for a businessTransaction.
        Deletes an existing businessTransaction tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_business_transaction_tag(business_transaction_id, business_transaction_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to remove tag from (required)
        :param str business_transaction_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id', 'business_transaction_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_business_transaction_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `delete_business_transaction_tag`")
        # verify the required parameter 'business_transaction_tag' is set
        if ('business_transaction_tag' not in params) or (params['business_transaction_tag'] is None):
            raise ValueError("Missing the required parameter `business_transaction_tag` when calling `delete_business_transaction_tag`")

        resource_path = '/beta/businessTransaction/{businessTransactionId}/tag/{businessTransactionTag}'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']
        if 'business_transaction_tag' in params:
            path_params['businessTransactionTag'] = params['business_transaction_tag']

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

    def get_business_transaction_by_filter(self, **kwargs):
        """
        Search businessTransactions by filter
        Returns the list of businessTransactions that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_business_transaction_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[BusinessTransaction]
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
                    " to method get_business_transaction_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/businessTransaction/search'.replace('{format}', 'json')
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
                                            response_type='list[BusinessTransaction]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_business_transaction_by_id(self, business_transaction_id, **kwargs):
        """
        Get a businessTransaction by id
        Returns the businessTransaction identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_business_transaction_by_id(business_transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to be returned. (required)
        :return: BusinessTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_business_transaction_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `get_business_transaction_by_id`")

        resource_path = '/beta/businessTransaction/{businessTransactionId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']

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
                                            response_type='BusinessTransaction',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_business_transaction_tags(self, business_transaction_id, **kwargs):
        """
        Get the tags for a businessTransaction.
        Get all existing businessTransaction tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_business_transaction_tags(business_transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_business_transaction_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `get_business_transaction_tags`")

        resource_path = '/beta/businessTransaction/{businessTransactionId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']

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

    def get_duplicate_business_transaction_by_id(self, business_transaction_id, **kwargs):
        """
        Get a duplicated a businessTransaction by id
        Returns a duplicated businessTransaction identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_business_transaction_by_id(business_transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int business_transaction_id: Id of the businessTransaction to be duplicated. (required)
        :return: BusinessTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_business_transaction_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_transaction_id' is set
        if ('business_transaction_id' not in params) or (params['business_transaction_id'] is None):
            raise ValueError("Missing the required parameter `business_transaction_id` when calling `get_duplicate_business_transaction_by_id`")

        resource_path = '/beta/businessTransaction/duplicate/{businessTransactionId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_transaction_id' in params:
            path_params['businessTransactionId'] = params['business_transaction_id']

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
                                            response_type='BusinessTransaction',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_business_transaction_custom_fields(self, body, **kwargs):
        """
        Update a businessTransaction custom fields
        Updates an existing businessTransaction custom fields using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_business_transaction_custom_fields(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BusinessTransaction body: BusinessTransaction to be updated. (required)
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
                    " to method update_business_transaction_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_business_transaction_custom_fields`")

        resource_path = '/beta/businessTransaction/customFields'.replace('{format}', 'json')
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
