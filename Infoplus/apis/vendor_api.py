# coding: utf-8

"""
VendorApi.py
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


class VendorApi(object):
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

    def add_vendor(self, body, **kwargs):
        """
        Create a vendor
        Inserts a new vendor using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_vendor(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Vendor body: Vendor to be inserted. (required)
        :return: Vendor
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
                    " to method add_vendor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_vendor`")

        resource_path = '/beta/vendor'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Vendor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_vendor_audit(self, vendor_id, vendor_audit, **kwargs):
        """
        Add new audit for a vendor
        Adds an audit to an existing vendor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_vendor_audit(vendor_id, vendor_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to add an audit to (required)
        :param str vendor_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id', 'vendor_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_vendor_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `add_vendor_audit`")
        # verify the required parameter 'vendor_audit' is set
        if ('vendor_audit' not in params) or (params['vendor_audit'] is None):
            raise ValueError("Missing the required parameter `vendor_audit` when calling `add_vendor_audit`")

        resource_path = '/beta/vendor/{vendorId}/audit/{vendorAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']
        if 'vendor_audit' in params:
            path_params['vendorAudit'] = params['vendor_audit']

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

    def add_vendor_tag(self, vendor_id, vendor_tag, **kwargs):
        """
        Add new tags for a vendor.
        Adds a tag to an existing vendor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_vendor_tag(vendor_id, vendor_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to add a tag to (required)
        :param str vendor_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id', 'vendor_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_vendor_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `add_vendor_tag`")
        # verify the required parameter 'vendor_tag' is set
        if ('vendor_tag' not in params) or (params['vendor_tag'] is None):
            raise ValueError("Missing the required parameter `vendor_tag` when calling `add_vendor_tag`")

        resource_path = '/beta/vendor/{vendorId}/tag/{vendorTag}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']
        if 'vendor_tag' in params:
            path_params['vendorTag'] = params['vendor_tag']

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

    def delete_vendor(self, vendor_id, **kwargs):
        """
        Delete a vendor
        Deletes the vendor identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_vendor(vendor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vendor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `delete_vendor`")

        resource_path = '/beta/vendor/{vendorId}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']

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

    def delete_vendor_tag(self, vendor_id, vendor_tag, **kwargs):
        """
        Delete a tag for a vendor.
        Deletes an existing vendor tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_vendor_tag(vendor_id, vendor_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to remove tag from (required)
        :param str vendor_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id', 'vendor_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vendor_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `delete_vendor_tag`")
        # verify the required parameter 'vendor_tag' is set
        if ('vendor_tag' not in params) or (params['vendor_tag'] is None):
            raise ValueError("Missing the required parameter `vendor_tag` when calling `delete_vendor_tag`")

        resource_path = '/beta/vendor/{vendorId}/tag/{vendorTag}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']
        if 'vendor_tag' in params:
            path_params['vendorTag'] = params['vendor_tag']

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

    def get_duplicate_vendor_by_id(self, vendor_id, **kwargs):
        """
        Get a duplicated a vendor by id
        Returns a duplicated vendor identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_vendor_by_id(vendor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to be duplicated. (required)
        :return: Vendor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_vendor_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `get_duplicate_vendor_by_id`")

        resource_path = '/beta/vendor/duplicate/{vendorId}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']

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
                                            response_type='Vendor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_vendor_by_filter(self, **kwargs):
        """
        Search vendors by filter
        Returns the list of vendors that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vendor_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[Vendor]
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
                    " to method get_vendor_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/vendor/search'.replace('{format}', 'json')
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
                                            response_type='list[Vendor]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_vendor_by_id(self, vendor_id, **kwargs):
        """
        Get a vendor by id
        Returns the vendor identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vendor_by_id(vendor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to be returned. (required)
        :return: Vendor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vendor_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `get_vendor_by_id`")

        resource_path = '/beta/vendor/{vendorId}'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']

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
                                            response_type='Vendor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_vendor_tags(self, vendor_id, **kwargs):
        """
        Get the tags for a vendor.
        Get all existing vendor tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_vendor_tags(vendor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int vendor_id: Id of the vendor to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vendor_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vendor_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `get_vendor_tags`")

        resource_path = '/beta/vendor/{vendorId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']

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

    def update_vendor(self, body, **kwargs):
        """
        Update a vendor
        Updates an existing vendor using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_vendor(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Vendor body: Vendor to be updated. (required)
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
                    " to method update_vendor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_vendor`")

        resource_path = '/beta/vendor'.replace('{format}', 'json')
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

    def update_vendor_custom_fields(self, body, **kwargs):
        """
        Update a vendor custom fields
        Updates an existing vendor custom fields using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_vendor_custom_fields(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Vendor body: Vendor to be updated. (required)
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
                    " to method update_vendor_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_vendor_custom_fields`")

        resource_path = '/beta/vendor/customFields'.replace('{format}', 'json')
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
