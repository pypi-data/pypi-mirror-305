from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.practice_area_create_request import PracticeAreaCreateRequest
from openapi_server.models.practice_area_list import PracticeAreaList
from openapi_server.models.practice_area_show import PracticeAreaShow
from openapi_server.models.practice_area_update_request import PracticeAreaUpdateRequest
from openapi_server import util


async def practice_area_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new PracticeArea

    Outlines the parameters and data fields used when creating a new PracticeArea

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Practice Areas
    :type body: dict | bytes

    """
    body = PracticeAreaCreateRequest.from_dict(body)
    return web.Response(status=200)


async def practice_area_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single PracticeArea

    Outlines the parameters, optional and required, used when deleting the record for a single PracticeArea

    :param id: The unique identifier for the PracticeArea.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def practice_area_index(request: web.Request, x_api_version=None, code=None, created_since=None, fields=None, ids=None, limit=None, matter_id=None, name=None, order=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all PracticeAreas

    Outlines the parameters, optional and required, used when requesting the data for all PracticeAreas

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param code: Filter PracticeArea records to those that match the given code.
    :type code: str
    :param created_since: Filter PracticeArea records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter PracticeArea records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter.
    :type matter_id: int
    :param name: Filter PracticeArea records to those that match the given name.
    :type name: str
    :param order: Orders the PracticeArea records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter PracticeArea records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def practice_area_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single PracticeArea

    Outlines the parameters, optional and required, used when requesting the data for a single PracticeArea

    :param id: The unique identifier for the PracticeArea.
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


async def practice_area_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single PracticeArea

    Outlines the parameters and data fields used when updating a single PracticeArea

    :param id: The unique identifier for the PracticeArea.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Practice Areas
    :type body: dict | bytes

    """
    body = PracticeAreaUpdateRequest.from_dict(body)
    return web.Response(status=200)
