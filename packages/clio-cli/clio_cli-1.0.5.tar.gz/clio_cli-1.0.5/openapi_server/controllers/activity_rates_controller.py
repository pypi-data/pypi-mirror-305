from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_rate_create_request import ActivityRateCreateRequest
from openapi_server.models.activity_rate_list import ActivityRateList
from openapi_server.models.activity_rate_show import ActivityRateShow
from openapi_server.models.error import Error
from openapi_server import util


async def activity_rate_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new ActivityRate

    Outlines the parameters and data fields used when creating a new ActivityRate

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activity Rates
    :type body: dict | bytes

    """
    body = ActivityRateCreateRequest.from_dict(body)
    return web.Response(status=200)


async def activity_rate_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single ActivityRate

    Outlines the parameters, optional and required, used when deleting the record for a single ActivityRate

    :param id: The unique identifier for the ActivityRate.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def activity_rate_index(request: web.Request, x_api_version=None, co_counsel_contact_id=None, contact_id=None, created_since=None, fields=None, ids=None, limit=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all ActivityRates

    Outlines the parameters, optional and required, used when requesting the data for all ActivityRates

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param co_counsel_contact_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.
    :type co_counsel_contact_id: int
    :param contact_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.
    :type contact_id: int
    :param created_since: Filter ActivityRate records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter ActivityRate records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of ActivityRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter ActivityRate records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def activity_rate_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ActivityRate

    Outlines the parameters, optional and required, used when requesting the data for a single ActivityRate

    :param id: The unique identifier for the ActivityRate.
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


async def activity_rate_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single ActivityRate

    Outlines the parameters and data fields used when updating a single ActivityRate

    :param id: The unique identifier for the ActivityRate.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activity Rates
    :type body: dict | bytes

    """
    body = ActivityRateCreateRequest.from_dict(body)
    return web.Response(status=200)
