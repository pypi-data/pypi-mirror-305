from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.report_preset_create_request import ReportPresetCreateRequest
from openapi_server.models.report_preset_list import ReportPresetList
from openapi_server.models.report_preset_show import ReportPresetShow
from openapi_server.models.report_preset_update_request import ReportPresetUpdateRequest
from openapi_server.models.report_show import ReportShow
from openapi_server import util


async def report_preset_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new ReportPreset

    Outlines the parameters and data fields used when creating a new ReportPreset

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Report Presets
    :type body: dict | bytes

    """
    body = ReportPresetCreateRequest.from_dict(body)
    return web.Response(status=200)


async def report_preset_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single ReportPreset

    Outlines the parameters, optional and required, used when deleting the record for a single ReportPreset

    :param id: The unique identifier for the ReportPreset.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def report_preset_generate_report(request: web.Request, id) -> web.Response:
    """Generate a new report for a given preset

    Generate a new report for a given preset

    :param id: The unique identifier for the ReportPreset.
    :type id: int

    """
    return web.Response(status=200)


async def report_preset_index(request: web.Request, x_api_version=None, category=None, created_since=None, fields=None, has_schedule=None, ids=None, limit=None, order=None, output_format=None, page_token=None, query=None, schedule_frequency=None, updated_since=None) -> web.Response:
    """Return the data for all ReportPresets

    Outlines the parameters, optional and required, used when requesting the data for all ReportPresets

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param category: Filters ReportPreset data by category.
    :type category: str
    :param created_since: Filter ReportPreset records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param has_schedule: Filters ReportPreset records to those that have or do not have a Report Schedule.
    :type has_schedule: bool
    :param ids: Filter ReportPreset records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of ReportPreset records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the ReportPreset records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param output_format: Filters ReportPreset data by format.
    :type output_format: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for ReportPreset name.
    :type query: str
    :param schedule_frequency: Filters ReportPreset records to those that have a Report Schedule of the specified frequency.
    :type schedule_frequency: str
    :param updated_since: Filter ReportPreset records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def report_preset_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ReportPreset

    Outlines the parameters, optional and required, used when requesting the data for a single ReportPreset

    :param id: The unique identifier for the ReportPreset.
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


async def report_preset_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single ReportPreset

    Outlines the parameters and data fields used when updating a single ReportPreset

    :param id: The unique identifier for the ReportPreset.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Report Presets
    :type body: dict | bytes

    """
    body = ReportPresetUpdateRequest.from_dict(body)
    return web.Response(status=200)
