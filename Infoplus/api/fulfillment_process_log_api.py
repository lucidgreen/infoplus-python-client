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


class FulfillmentProcessLogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_fulfillment_process_log_audit(self, fulfillment_process_log_id, fulfillment_process_log_audit, **kwargs):  # noqa: E501
        """Add new audit for a fulfillmentProcessLog  # noqa: E501

        Adds an audit to an existing fulfillmentProcessLog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_fulfillment_process_log_audit(fulfillment_process_log_id, fulfillment_process_log_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to add an audit to (required)
        :param str fulfillment_process_log_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_fulfillment_process_log_audit_with_http_info(fulfillment_process_log_id, fulfillment_process_log_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_fulfillment_process_log_audit_with_http_info(fulfillment_process_log_id, fulfillment_process_log_audit, **kwargs)  # noqa: E501
            return data

    def add_fulfillment_process_log_audit_with_http_info(self, fulfillment_process_log_id, fulfillment_process_log_audit, **kwargs):  # noqa: E501
        """Add new audit for a fulfillmentProcessLog  # noqa: E501

        Adds an audit to an existing fulfillmentProcessLog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_fulfillment_process_log_audit_with_http_info(fulfillment_process_log_id, fulfillment_process_log_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to add an audit to (required)
        :param str fulfillment_process_log_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id', 'fulfillment_process_log_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_fulfillment_process_log_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `add_fulfillment_process_log_audit`")  # noqa: E501
        # verify the required parameter 'fulfillment_process_log_audit' is set
        if ('fulfillment_process_log_audit' not in params or
                params['fulfillment_process_log_audit'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_audit` when calling `add_fulfillment_process_log_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501
        if 'fulfillment_process_log_audit' in params:
            path_params['fulfillmentProcessLogAudit'] = params['fulfillment_process_log_audit']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/audit/{fulfillmentProcessLogAudit}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_fulfillment_process_log_tag(self, fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs):  # noqa: E501
        """Add new tags for a fulfillmentProcessLog.  # noqa: E501

        Adds a tag to an existing fulfillmentProcessLog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to add a tag to (required)
        :param str fulfillment_process_log_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs)  # noqa: E501
            return data

    def add_fulfillment_process_log_tag_with_http_info(self, fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs):  # noqa: E501
        """Add new tags for a fulfillmentProcessLog.  # noqa: E501

        Adds a tag to an existing fulfillmentProcessLog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to add a tag to (required)
        :param str fulfillment_process_log_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id', 'fulfillment_process_log_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_fulfillment_process_log_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `add_fulfillment_process_log_tag`")  # noqa: E501
        # verify the required parameter 'fulfillment_process_log_tag' is set
        if ('fulfillment_process_log_tag' not in params or
                params['fulfillment_process_log_tag'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_tag` when calling `add_fulfillment_process_log_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501
        if 'fulfillment_process_log_tag' in params:
            path_params['fulfillmentProcessLogTag'] = params['fulfillment_process_log_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag/{fulfillmentProcessLogTag}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_fulfillment_process_log_tag(self, fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs):  # noqa: E501
        """Delete a tag for a fulfillmentProcessLog.  # noqa: E501

        Deletes an existing fulfillmentProcessLog tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to remove tag from (required)
        :param str fulfillment_process_log_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs)  # noqa: E501
            return data

    def delete_fulfillment_process_log_tag_with_http_info(self, fulfillment_process_log_id, fulfillment_process_log_tag, **kwargs):  # noqa: E501
        """Delete a tag for a fulfillmentProcessLog.  # noqa: E501

        Deletes an existing fulfillmentProcessLog tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fulfillment_process_log_tag_with_http_info(fulfillment_process_log_id, fulfillment_process_log_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to remove tag from (required)
        :param str fulfillment_process_log_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id', 'fulfillment_process_log_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fulfillment_process_log_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `delete_fulfillment_process_log_tag`")  # noqa: E501
        # verify the required parameter 'fulfillment_process_log_tag' is set
        if ('fulfillment_process_log_tag' not in params or
                params['fulfillment_process_log_tag'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_tag` when calling `delete_fulfillment_process_log_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501
        if 'fulfillment_process_log_tag' in params:
            path_params['fulfillmentProcessLogTag'] = params['fulfillment_process_log_tag']  # noqa: E501

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
            '/beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag/{fulfillmentProcessLogTag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_duplicate_fulfillment_process_log_by_id(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get a duplicated a fulfillmentProcessLog by id  # noqa: E501

        Returns a duplicated fulfillmentProcessLog identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_fulfillment_process_log_by_id(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to be duplicated. (required)
        :return: FulfillmentProcessLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_fulfillment_process_log_by_id_with_http_info(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get a duplicated a fulfillmentProcessLog by id  # noqa: E501

        Returns a duplicated fulfillmentProcessLog identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to be duplicated. (required)
        :return: FulfillmentProcessLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_fulfillment_process_log_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `get_duplicate_fulfillment_process_log_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501

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
            '/beta/fulfillmentProcessLog/duplicate/{fulfillmentProcessLogId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FulfillmentProcessLog',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fulfillment_process_log_by_filter(self, **kwargs):  # noqa: E501
        """Search fulfillmentProcessLogs by filter  # noqa: E501

        Returns the list of fulfillmentProcessLogs that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[FulfillmentProcessLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fulfillment_process_log_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_process_log_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fulfillment_process_log_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search fulfillmentProcessLogs by filter  # noqa: E501

        Returns the list of fulfillmentProcessLogs that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[FulfillmentProcessLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page', 'limit', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_process_log_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

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
            '/beta/fulfillmentProcessLog/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FulfillmentProcessLog]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fulfillment_process_log_by_id(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get a fulfillmentProcessLog by id  # noqa: E501

        Returns the fulfillmentProcessLog identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_by_id(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to be returned. (required)
        :return: FulfillmentProcessLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_process_log_by_id_with_http_info(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get a fulfillmentProcessLog by id  # noqa: E501

        Returns the fulfillmentProcessLog identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_by_id_with_http_info(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to be returned. (required)
        :return: FulfillmentProcessLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_process_log_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `get_fulfillment_process_log_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501

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
            '/beta/fulfillmentProcessLog/{fulfillmentProcessLogId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FulfillmentProcessLog',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fulfillment_process_log_tags(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get the tags for a fulfillmentProcessLog.  # noqa: E501

        Get all existing fulfillmentProcessLog tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_tags(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fulfillment_process_log_tags_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_process_log_tags_with_http_info(fulfillment_process_log_id, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_process_log_tags_with_http_info(self, fulfillment_process_log_id, **kwargs):  # noqa: E501
        """Get the tags for a fulfillmentProcessLog.  # noqa: E501

        Get all existing fulfillmentProcessLog tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fulfillment_process_log_tags_with_http_info(fulfillment_process_log_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fulfillment_process_log_id: Id of the fulfillmentProcessLog to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fulfillment_process_log_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_process_log_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fulfillment_process_log_id' is set
        if ('fulfillment_process_log_id' not in params or
                params['fulfillment_process_log_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_process_log_id` when calling `get_fulfillment_process_log_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_process_log_id' in params:
            path_params['fulfillmentProcessLogId'] = params['fulfillment_process_log_id']  # noqa: E501

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
            '/beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
