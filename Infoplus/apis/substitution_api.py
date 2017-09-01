# coding: utf-8

"""
SubstitutionApi.py
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


class SubstitutionApi(object):
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

    def add_substitution(self, body, **kwargs):
        """
        Create a substitution
        Inserts a new substitution using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_substitution(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Substitution body: Substitution to be inserted. (required)
        :return: Substitution
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
                    " to method add_substitution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_substitution`")

        resource_path = '/beta/substitution'.replace('{format}', 'json')
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
                                            response_type='Substitution',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_substitution_audit(self, substitution_id, substitution_audit, **kwargs):
        """
        Add new audit for a substitution
        Adds an audit to an existing substitution.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_substitution_audit(substitution_id, substitution_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to add an audit to (required)
        :param str substitution_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id', 'substitution_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_substitution_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `add_substitution_audit`")
        # verify the required parameter 'substitution_audit' is set
        if ('substitution_audit' not in params) or (params['substitution_audit'] is None):
            raise ValueError("Missing the required parameter `substitution_audit` when calling `add_substitution_audit`")

        resource_path = '/beta/substitution/{substitutionId}/audit/{substitutionAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']
        if 'substitution_audit' in params:
            path_params['substitutionAudit'] = params['substitution_audit']

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

    def add_substitution_tag(self, substitution_id, substitution_tag, **kwargs):
        """
        Add new tags for a substitution.
        Adds a tag to an existing substitution.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_substitution_tag(substitution_id, substitution_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to add a tag to (required)
        :param str substitution_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id', 'substitution_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_substitution_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `add_substitution_tag`")
        # verify the required parameter 'substitution_tag' is set
        if ('substitution_tag' not in params) or (params['substitution_tag'] is None):
            raise ValueError("Missing the required parameter `substitution_tag` when calling `add_substitution_tag`")

        resource_path = '/beta/substitution/{substitutionId}/tag/{substitutionTag}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']
        if 'substitution_tag' in params:
            path_params['substitutionTag'] = params['substitution_tag']

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

    def delete_substitution(self, substitution_id, **kwargs):
        """
        Delete a substitution
        Deletes the substitution identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_substitution(substitution_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_substitution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `delete_substitution`")

        resource_path = '/beta/substitution/{substitutionId}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']

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

    def delete_substitution_tag(self, substitution_id, substitution_tag, **kwargs):
        """
        Delete a tag for a substitution.
        Deletes an existing substitution tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_substitution_tag(substitution_id, substitution_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to remove tag from (required)
        :param str substitution_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id', 'substitution_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_substitution_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `delete_substitution_tag`")
        # verify the required parameter 'substitution_tag' is set
        if ('substitution_tag' not in params) or (params['substitution_tag'] is None):
            raise ValueError("Missing the required parameter `substitution_tag` when calling `delete_substitution_tag`")

        resource_path = '/beta/substitution/{substitutionId}/tag/{substitutionTag}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']
        if 'substitution_tag' in params:
            path_params['substitutionTag'] = params['substitution_tag']

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

    def get_duplicate_substitution_by_id(self, substitution_id, **kwargs):
        """
        Get a duplicated a substitution by id
        Returns a duplicated substitution identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_substitution_by_id(substitution_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to be duplicated. (required)
        :return: Substitution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_substitution_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `get_duplicate_substitution_by_id`")

        resource_path = '/beta/substitution/duplicate/{substitutionId}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']

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
                                            response_type='Substitution',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_substitution_by_filter(self, **kwargs):
        """
        Search substitutions by filter
        Returns the list of substitutions that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_substitution_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[Substitution]
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
                    " to method get_substitution_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/substitution/search'.replace('{format}', 'json')
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
                                            response_type='list[Substitution]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_substitution_by_id(self, substitution_id, **kwargs):
        """
        Get a substitution by id
        Returns the substitution identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_substitution_by_id(substitution_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to be returned. (required)
        :return: Substitution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_substitution_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `get_substitution_by_id`")

        resource_path = '/beta/substitution/{substitutionId}'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']

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
                                            response_type='Substitution',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_substitution_tags(self, substitution_id, **kwargs):
        """
        Get the tags for a substitution.
        Get all existing substitution tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_substitution_tags(substitution_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int substitution_id: Id of the substitution to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['substitution_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_substitution_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'substitution_id' is set
        if ('substitution_id' not in params) or (params['substitution_id'] is None):
            raise ValueError("Missing the required parameter `substitution_id` when calling `get_substitution_tags`")

        resource_path = '/beta/substitution/{substitutionId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'substitution_id' in params:
            path_params['substitutionId'] = params['substitution_id']

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

    def update_substitution(self, body, **kwargs):
        """
        Update a substitution
        Updates an existing substitution using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_substitution(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Substitution body: Substitution to be updated. (required)
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
                    " to method update_substitution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_substitution`")

        resource_path = '/beta/substitution'.replace('{format}', 'json')
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

    def update_substitution_custom_fields(self, body, **kwargs):
        """
        Update a substitution custom fields
        Updates an existing substitution custom fields using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_substitution_custom_fields(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Substitution body: Substitution to be updated. (required)
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
                    " to method update_substitution_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_substitution_custom_fields`")

        resource_path = '/beta/substitution/customFields'.replace('{format}', 'json')
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