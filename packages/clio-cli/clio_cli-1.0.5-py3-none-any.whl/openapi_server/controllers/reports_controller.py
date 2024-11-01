from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.report_create_request import ReportCreateRequest
from openapi_server.models.report_list import ReportList
from openapi_server.models.report_show import ReportShow
from openapi_server import util


async def report_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Report

    Outlines the parameters and data fields used when creating a new Report

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Reports
    :type body: dict | bytes

    """
    body = ReportCreateRequest.from_dict(body)
    return web.Response(status=200)


async def report_download(request: web.Request, id) -> web.Response:
    """Download the completed Report

    Download the completed Report

    :param id: The unique identifier for the Report.
    :type id: int

    """
    return web.Response(status=200)


async def report_index(request: web.Request, x_api_version=None, category=None, created_before=None, created_since=None, fields=None, ids=None, kind=None, limit=None, output_format=None, page_token=None, query=None, source=None, state=None, updated_since=None) -> web.Response:
    """Return the data for all Reports

    Outlines the parameters, optional and required, used when requesting the data for all Reports

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param category: Filters Report data by category.
    :type category: str
    :param created_before: Filters Report data by date. (Expects an ISO-8601 date).
    :type created_before: str
    :param created_since: Filter Report records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Report records to those having the specified unique identifiers.
    :type ids: int
    :param kind: Filters Report data by kind.
    :type kind: str
    :param limit: A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param output_format: Filters Report data by format.
    :type output_format: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for Report name.
    :type query: str
    :param source: Filters Report data by source.
    :type source: str
    :param state: Filters Report data by state.
    :type state: str
    :param updated_since: Filter Report records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def report_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Report

    Outlines the parameters, optional and required, used when requesting the data for a single Report

    :param id: The unique identifier for the Report.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)
