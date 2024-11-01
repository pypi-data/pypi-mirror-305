from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_server.models.grant_funding_source_list import GrantFundingSourceList
from openapi_server.models.grant_funding_source_show import GrantFundingSourceShow
from openapi_server import util


async def grant_funding_source_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new grant funding source

    Outlines the parameters and data fields used when creating a new GrantFundingSource

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Grant Funding Sources
    :type body: dict | bytes

    """
    body = GrantFundingSourceCreateRequest.from_dict(body)
    return web.Response(status=200)


async def grant_funding_source_destroy(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Delete a single grant funding source

    Outlines the parameters and data fields used when updating a single GrantFundingSource

    :param id: The unique identifier for the GrantFundingSource.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Grant Funding Sources
    :type body: dict | bytes

    """
    body = GrantFundingSourceCreateRequest.from_dict(body)
    return web.Response(status=200)


async def grant_funding_source_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, name=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all grant funding sources

    Outlines the parameters, optional and required, used when requesting the data for all GrantFundingSources

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter GrantFundingSource records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter GrantFundingSource records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param name: Filter GrantFundingSource records to those that match the given name.
    :type name: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter GrantFundingSource records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def grant_funding_source_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single grant funding source

    Outlines the parameters and data fields used when updating a single GrantFundingSource

    :param id: The unique identifier for the GrantFundingSource.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Grant Funding Sources
    :type body: dict | bytes

    """
    body = GrantFundingSourceCreateRequest.from_dict(body)
    return web.Response(status=200)
