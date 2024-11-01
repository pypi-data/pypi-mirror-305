from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_description_create_request import ActivityDescriptionCreateRequest
from openapi_server.models.activity_description_list import ActivityDescriptionList
from openapi_server.models.activity_description_show import ActivityDescriptionShow
from openapi_server.models.activity_description_update_request import ActivityDescriptionUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def activity_description_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new ActivityDescription

    Outlines the parameters and data fields used when creating a new ActivityDescription

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activity Descriptions
    :type body: dict | bytes

    """
    body = ActivityDescriptionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def activity_description_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single ActivityDescription

    Outlines the parameters, optional and required, used when deleting the record for a single ActivityDescription

    :param id: The unique identifier for the ActivityDescription.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def activity_description_index(request: web.Request, x_api_version=None, created_since=None, fields=None, flat_rate=None, ids=None, limit=None, page_token=None, rate_for_matter_id=None, rate_for_user_id=None, type=None, updated_since=None, user_id=None) -> web.Response:
    """Return the data for all ActivityDescriptions

    Outlines the parameters, optional and required, used when requesting the data for all ActivityDescriptions

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter ActivityDescription records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param flat_rate: Filter ActivityDescription records to those that have a flat rate, or not.
    :type flat_rate: bool
    :param ids: Filter ActivityDescription records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of ActivityDescription records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param rate_for_matter_id: Matter id for rate calculation.
    :type rate_for_matter_id: int
    :param rate_for_user_id: User id for rate calculation. If not provided, the user associated to the API request is assumed.
    :type rate_for_user_id: int
    :param type: Filter ActivityDescription records to those of a specific type.
    :type type: str
    :param updated_since: Filter ActivityDescription records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param user_id: The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityDescription records with the matching property.
    :type user_id: int

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def activity_description_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ActivityDescription

    Outlines the parameters, optional and required, used when requesting the data for a single ActivityDescription

    :param id: The unique identifier for the ActivityDescription.
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


async def activity_description_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single ActivityDescription

    Outlines the parameters and data fields used when updating a single ActivityDescription

    :param id: The unique identifier for the ActivityDescription.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activity Descriptions
    :type body: dict | bytes

    """
    body = ActivityDescriptionUpdateRequest.from_dict(body)
    return web.Response(status=200)
