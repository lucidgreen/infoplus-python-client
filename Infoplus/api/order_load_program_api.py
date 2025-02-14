# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Infoplus.api_client import ApiClient


class OrderLoadProgramApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_order_load_program_by_search_text(self, **kwargs):  # noqa: E501
        """Search orderLoadPrograms  # noqa: E501

        Returns the list of orderLoadPrograms that match the given searchText.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_order_load_program_by_search_text(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param str search_text: Search text, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :return: list[OrderLoadProgram]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_order_load_program_by_search_text_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_order_load_program_by_search_text_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_order_load_program_by_search_text_with_http_info(self, **kwargs):  # noqa: E501
        """Search orderLoadPrograms  # noqa: E501

        Returns the list of orderLoadPrograms that match the given searchText.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_order_load_program_by_search_text_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param str search_text: Search text, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :return: list[OrderLoadProgram]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_text', 'page', 'limit']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_load_program_by_search_text" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_text' in params:
            query_params.append(('searchText', params['search_text']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/orderLoadProgram/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OrderLoadProgram]',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_req_load_program_by_id(self, order_load_program_id, **kwargs):  # noqa: E501
        """Get an orderLoadProgram by id  # noqa: E501

        Returns the orderLoadProgram identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_req_load_program_by_id(order_load_program_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param str order_load_program_id: Id of orderLoadProgram to be returned. (required)
        :return: OrderLoadProgram
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_req_load_program_by_id_with_http_info(order_load_program_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_req_load_program_by_id_with_http_info(order_load_program_id, **kwargs)  # noqa: E501
            return data

    def get_req_load_program_by_id_with_http_info(self, order_load_program_id, **kwargs):  # noqa: E501
        """Get an orderLoadProgram by id  # noqa: E501

        Returns the orderLoadProgram identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_req_load_program_by_id_with_http_info(order_load_program_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param str order_load_program_id: Id of orderLoadProgram to be returned. (required)
        :return: OrderLoadProgram
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_load_program_id']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_req_load_program_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_load_program_id' is set
        if ('order_load_program_id' not in params or
                params['order_load_program_id'] is None):
            raise ValueError("Missing the required parameter `order_load_program_id` when calling `get_req_load_program_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_load_program_id' in params:
            path_params['orderLoadProgramId'] = params['order_load_program_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/orderLoadProgram/{orderLoadProgramId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderLoadProgram',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
