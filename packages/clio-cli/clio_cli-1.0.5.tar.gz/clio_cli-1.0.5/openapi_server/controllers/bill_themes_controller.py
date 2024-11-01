from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_theme_list import BillThemeList
from openapi_server.models.bill_theme_show import BillThemeShow
from openapi_server.models.bill_theme_update_request import BillThemeUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def bill_theme_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all BillThemes

    Outlines the parameters, optional and required, used when requesting the data for all BillThemes

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter BillTheme records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter BillTheme records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of BillTheme records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter BillTheme records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def bill_theme_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single BillTheme

    Outlines the parameters and data fields used when updating a single BillTheme

    :param id: The unique identifier for the BillTheme.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Bill Themes
    :type body: dict | bytes

    """
    body = BillThemeUpdateRequest.from_dict(body)
    return web.Response(status=200)
