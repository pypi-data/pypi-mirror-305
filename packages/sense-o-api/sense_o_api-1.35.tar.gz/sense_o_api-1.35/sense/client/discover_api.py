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
class DiscoverApi():
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    def __init__(self, req_wrapper=None):
        if req_wrapper is None:
            self.client = RequestWrapper()
        else:
            self.client = req_wrapper

    def discover_domain_id_get(self, domain_id, **kwargs):  # noqa: E501
        """Edge points discover and description for a specific domain  # noqa: E501

        List all associated edge points (and capabilities)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_get(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_domain_id_get_with_http_info(
                domain_id, **kwargs)  # noqa: E501
        (data) = self.discover_domain_id_get_with_http_info(
            domain_id, **kwargs)  # noqa: E501
        return data

    def discover_domain_id_get_with_http_info(self, domain_id,
                                              **kwargs):  # noqa: E501
        """Edge points discover and description for a specific domain  # noqa: E501

        List all associated edge points (and capabilities)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_get_with_http_info(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_domain_id_get")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or params['domain_id'] is None):
            raise ValueError(
                "Missing the required parameter `domain_id` when calling `discover_domain_id_get`"
            )  # noqa: E501

        return self.client.request('GET', f'/discover/{domain_id}')

    def discover_domain_id_peers_get(self, domain_id, **kwargs):  # noqa: E501
        """edge points discover and description of peer domain for a given domain or end-site  # noqa: E501

        List peer domain edge points (and capabilities) that connect this domain (by URI or name)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_peers_get(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target end-site domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_domain_id_peers_get_with_http_info(
                domain_id, **kwargs)  # noqa: E501
        (data) = self.discover_domain_id_peers_get_with_http_info(
            domain_id, **kwargs)  # noqa: E501
        return data

    def discover_domain_id_peers_get_with_http_info(self, domain_id,
                                                    **kwargs):  # noqa: E501
        """edge points discover and description of peer domain for a given domain or end-site  # noqa: E501

        List peer domain edge points (and capabilities) that connect this domain (by URI or name)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_peers_get_with_http_info(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target end-site domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_domain_id_peers_get")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or params['domain_id'] is None):
            raise ValueError(
                "Missing the required parameter `domain_id` when calling `discover_domain_id_peers_get`"
            )  # noqa: E501

        return self.client.request('GET', f'/discover/{domain_id}/peers')

    def discover_domain_id_ipv6pool_get(self, domain_id, **kwargs):  # noqa: E501
        """ discover and description of ipv6 subnet pool for a given domain or end-site  # noqa: E501

        List of ipv6 subnet pools for this domain (by URI or name)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_ipv6pool_get(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target end-site domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_domain_id_ipv6pool_get_with_http_info(
                domain_id, **kwargs)  # noqa: E501
        (data) = self.discover_domain_id_ipv6pool_get_with_http_info(
            domain_id, **kwargs)  # noqa: E501
        return data

    def discover_domain_id_ipv6pool_get_with_http_info(self, domain_id,
                                                    **kwargs):  # noqa: E501
        """ discover and description of ipv6 subnet pool for a given domain or end-site  # noqa: E501

        List of ipv6 subnet pools for this domain (by URI or name)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domain_id_ipv6pool_get_with_http_info(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Name of URI of a target end-site domain (required)
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_domain_id_ipv6pool_get")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or params['domain_id'] is None):
            raise ValueError(
                "Missing the required parameter `domain_id` when calling `discover_domain_id_ipv6pool_get`"
            )  # noqa: E501

        return self.client.request('GET', f'/discover/{domain_id}/ipv6pool')

    def discover_domains_get(self, **kwargs):  # noqa: E501
        """Topology domains  # noqa: E501

        List all known domains (and capabilities?)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domains_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_domains_get_with_http_info(
                **kwargs)  # noqa: E501
        (data) = self.discover_domains_get_with_http_info(
            **kwargs)  # noqa: E501
        return data

    def discover_domains_get_with_http_info(self, **kwargs):  # noqa: E501
        """Topology domains  # noqa: E501

        List all known domains (and capabilities?)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_domains_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
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
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_domains_get")
            params[key] = val
        del params['kwargs']
        return self.client.request('GET', '/discover/domains')

    def discover_get(self, **kwargs):  # noqa: E501
        """Topology domains, edge points and peers information  # noqa: E501

        List global domain information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_get_with_http_info(**kwargs)  # noqa: E501
        (data) = self.discover_get_with_http_info(**kwargs)  # noqa: E501
        return data

    def discover_get_with_http_info(self, **kwargs):  # noqa: E501
        """Topology domains, edge points and peers information  # noqa: E501

        List global domain information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
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
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_get")
            params[key] = val
        del params['kwargs']
        return self.client.request('GET', '/discover')

    def discover_lookup_name_get(self, name, **kwargs):  # noqa: E501
        """Look up for domain / node / port URI by name  # noqa: E501

        List of URI string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_lookup_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Resource nml:name or mrs:NetworkAddress or 'fqdn' type (required)
        :param str search: search by name, tag or NetworkAddress .
        :param str type: type of tag or NetworkAddress
        :param bool regex: use full name march or regex
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_lookup_name_get_with_http_info(
                name, **kwargs)  # noqa: E501
        (data) = self.discover_lookup_name_get_with_http_info(
            name, **kwargs)  # noqa: E501
        return data

    def discover_lookup_name_get_with_http_info(self, name,
                                                **kwargs):  # noqa: E501
        """Look up for domain / node / port URI by name  # noqa: E501

        List of URI string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_lookup_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Resource nml:name or mrs:NetworkAddress or 'fqdn' type (required)
        :param str search: search by name, tag or NetworkAddress .
        :param str type: type of tag or NetworkAddress
        :param bool regex: use full name march or regex
        :return: DomainDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'search', 'type', 'regex']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_lookup_name_get")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or params['name'] is None):
            raise ValueError(
                "Missing the required parameter `name` when calling `discover_lookup_name_get`"
            )  # noqa: E501

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'regex' in params:
            query_params.append(('regex', params['regex']))  # noqa: E501

        return self.client.request('GET',
                                   f'/discover/lookup/{name}',
                                   query_params=query_params)

    def discover_lookup_rooturi_get(self, uri, **kwargs):  # noqa: E501
        """Look up for domain root URI by given a resource URI  # noqa: E501

        List of URI string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_lookup_rooturi_get(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Resource URI (required)
        :return: URI string
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_lookup_rooturi_get_with_http_info(
                uri, **kwargs)  # noqa: E501
        (data) = self.discover_lookup_rooturi_get_with_http_info(
            uri, **kwargs)  # noqa: E501
        return data

    def discover_lookup_rooturi_get_with_http_info(self, uri,
                                                **kwargs):  # noqa: E501
        """Look up for domain root URI by given a resource URI  # noqa: E501

        List of URI string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_lookup_rooturi_get(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Resource URI (required)
        :return: URI string
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_lookup_name_get")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('uri' not in params or params['uri'] is None):
            raise ValueError(
                "Missing the required parameter `uri` when calling `discover_lookup_rooturi_get`"
            )  # noqa: E501

        query_params = []

        return self.client.request('GET',
                                   f'/discover/lookup/{uri}/rooturi',
                                   query_params=query_params)

    def discover_service_instances_get(self, **kwargs):  # noqa: E501
        """Service discover and description  # noqa: E501

        List service instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_service_instances_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: search by name substring or regex
        :param bool regex: use substring march or regex
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.discover_service_instances_get_with_http_info(
                **kwargs)  # noqa: E501
        (data) = self.discover_service_instances_get_with_http_info(
            **kwargs)  # noqa: E501
        return data

    def discover_service_instances_get_with_http_info(self,
                                                      **kwargs):  # noqa: E501
        """Service discover and description  # noqa: E501

        List service instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.discover_service_instances_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: search by name substring or regex
        :param bool regex: use substring march or regex
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'regex']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument '{key}'"
                                " to method discover_service_instances_get")
            params[key] = val
        del params['kwargs']

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'regex' in params:
            query_params.append(('regex', params['regex']))  # noqa: E501
        return self.client.request('GET',
                                   '/discover/service/instances',
                                   query_params=query_params)
