#!/usr/bin/env python3
# coding: utf-8
"""
    SENSE-O Northbound Intent API

    StackV SENSE-O Northbound REST API Documentation  # noqa: E501

    OpenAPI spec version: 2.0.2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from sense.client.requestwrapper import RequestWrapper
from sense.common import classwrapper

@classwrapper
class LoggingApi():
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    def __init__(self, req_wrapper=None):
        if req_wrapper is None:
            self.client = RequestWrapper()
        else:
            self.client = req_wrapper
        if 'SI_UUID' in self.client.config:
            self.si_uuid = self.client.config['SI_UUID']
        else:
            self.si_uuid = None

    def logging_set_archive_days(self, days, **kwargs):  # noqa: E501
        """Archive logs  # noqa: E501

        Archives all logs older than specified number of days.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_set_archive_days(days, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float days: Number of days. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logging_archive_days_put_with_http_info(
                days, **kwargs)  # noqa: E501
        else:
            (data) = self.logging_archive_days_put_with_http_info(
                days, **kwargs)  # noqa: E501
            return data

    def logging_archive_days_put_with_http_info(self, days,
                                                **kwargs):  # noqa: E501
        """Archive logs  # noqa: E501

        Archives all logs older than specified number of days.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_archive_days_put_with_http_info(days, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float days: Number of days. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['days']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method logging_archive_days_put" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'days' is set
        if ('days' not in params or params['days'] is None):
            raise ValueError(
                "Missing the required parameter `days` when calling `logging_archive_days_put`"
            )  # noqa: E501

        path_params = {}
        if 'days' in params:
            path_params['days'] = params['days']  # noqa: E501

        return self.client.request('PUT', f'/logging/archive/{days}')

    def logging_get_config(self, **kwargs):  # noqa: E501
        """Get logging configuration  # noqa: E501

        Retrieves the logging levels for each layer as well as database usage metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_get_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoggingConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logging_config_get_with_http_info(**
                                                          kwargs)  # noqa: E501
        else:
            (data
             ) = self.logging_config_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def logging_config_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get logging configuration  # noqa: E501

        Retrieves the logging levels for each layer as well as database usage metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_config_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: LoggingConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method logging_config_get" % key)
            params[key] = val
        del params['kwargs']

        return self.client.request('GET', f'/logging/config')

    def logging_set_logger_level(self, logger, level, **kwargs):  # noqa: E501
        """Set logger level  # noqa: E501

        Updates the logging level of the specified layer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_set_logger_level(logger, level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logger: Logging appender layer. (required)
        :param str level: Logging appender level. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logging_config_logger_level_put_with_http_info(
                logger, level, **kwargs)  # noqa: E501
        else:
            (data) = self.logging_config_logger_level_put_with_http_info(
                logger, level, **kwargs)  # noqa: E501
            return data

    def logging_config_logger_level_put_with_http_info(self, logger, level,
                                                       **kwargs):  # noqa: E501
        """Set logger level  # noqa: E501

        Updates the logging level of the specified layer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_config_logger_level_put_with_http_info(logger, level, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str logger: Logging appender layer. (required)
        :param str level: Logging appender level. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['logger', 'level']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method logging_config_logger_level_put" %
                                key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'logger' is set
        if ('logger' not in params or params['logger'] is None):
            raise ValueError(
                "Missing the required parameter `logger` when calling `logging_config_logger_level_put`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if ('level' not in params or params['level'] is None):
            raise ValueError(
                "Missing the required parameter `level` when calling `logging_config_logger_level_put`"
            )  # noqa: E501

        path_params = {}
        if 'logger' in params:
            path_params['logger'] = params['logger']  # noqa: E501
        if 'level' in params:
            path_params['level'] = params['level']  # noqa: E501

        return self.client.request('PUT', f'/logging/config/{logger}/{level}')

    def logging_set_filter(self, **kwargs):  # noqa: E501
        """Set logger filter  # noqa: E501

        Updates the logging filter with a new configuration string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_set_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Configuration string. "Use raw" will filter over the raw logging message before processing, and "pattern" is the regex itself.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logging_filter_put_with_http_info(**
                                                          kwargs)  # noqa: E501
        else:
            (data
             ) = self.logging_filter_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def logging_filter_put_with_http_info(self, **kwargs):  # noqa: E501
        """Set logger filter  # noqa: E501

        Updates the logging filter with a new configuration string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_filter_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Configuration string. "Use raw" will filter over the raw logging message before processing, and "pattern" is the regex itself.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method logging_filter_put" % key)
            params[key] = val
        del params['kwargs']

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.client.request('PUT',
                                   f'/logging/filter',
                                   body_params=body_params)

    def instance_get_logging(self, **kwargs):  # noqa: E501
        """Retrieve intents by service instance  # noqa: E501

        Queries all service intents belonging to given instance UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default.
        :param async_req bool
        :param str si_uuid: Intent UUID. (required)
        :return: list[IntentExpanded]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if self.si_uuid:
            kwargs['si_uuid'] = self.si_uuid
        if not kwargs['si_uuid'] :
            raise ValueError("Missing the required parameter `si_uuid`")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logging_logs_si_uuid_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logging_logs_si_uuid_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def logging_logs_si_uuid_get_with_http_info(self,
                                                **kwargs):  # noqa: E501
        """Retrieve intents by service instance  # noqa: E501

        Queries all service intents belonging to given instance UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logging_logs_si_uuid_get_with_http_info(si_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str si_uuid: Intent UUID. (required)
        :return: list[IntentExpanded]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['si_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logging_logs_si_uuid_get_with_http_info" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'si_uuid' is set
        if ('si_uuid' not in params or params['si_uuid'] is None):
            raise ValueError(
                "Missing the required parameter `si_uuid` when calling `logging_logs_si_uuid_get_with_http_info`"
            )  # noqa: E501

        return self.client.request('GET', '/logging/logs/' + kwargs['si_uuid'])
