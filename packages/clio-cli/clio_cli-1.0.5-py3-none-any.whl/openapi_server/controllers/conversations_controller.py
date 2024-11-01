from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_list import ConversationList
from openapi_server.models.conversation_show import ConversationShow
from openapi_server.models.conversation_update_request import ConversationUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def conversation_index(request: web.Request, x_api_version=None, archived=None, contact_id=None, created_since=None, _date=None, fields=None, for_user=None, ids=None, limit=None, matter_id=None, order=None, page_token=None, read_status=None, time_entries=None, updated_since=None) -> web.Response:
    """Return the data for all Conversations

    Outlines the parameters, optional and required, used when requesting the data for all Conversations

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param archived: Filter archived Conversation records.
    :type archived: bool
    :param contact_id: Filter Conversation records for the contact.
    :type contact_id: int
    :param created_since: Filter Conversation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param _date: Filter Conversation records created on a given date. (Expects an ISO-8601 date).
    :type _date: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param for_user: If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member. 
    :type for_user: bool
    :param ids: Filter Conversation records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property.
    :type matter_id: int
    :param order: Orders the Conversation records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param read_status: Filter Conversation records to those which have been read.
    :type read_status: bool
    :param time_entries: Filter Conversation records to those with or without associated time entries.
    :type time_entries: bool
    :param updated_since: Filter Conversation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    _date = util.deserialize_date(_date)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def conversation_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Conversation

    Outlines the parameters, optional and required, used when requesting the data for a single Conversation

    :param id: The unique identifier for the Conversation.
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


async def conversation_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Conversation

    Outlines the parameters and data fields used when updating a single Conversation

    :param id: The unique identifier for the Conversation.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Conversations
    :type body: dict | bytes

    """
    body = ConversationUpdateRequest.from_dict(body)
    return web.Response(status=200)
