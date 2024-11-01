from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_message_create_request import ConversationMessageCreateRequest
from openapi_server.models.conversation_message_list import ConversationMessageList
from openapi_server.models.conversation_message_show import ConversationMessageShow
from openapi_server.models.error import Error
from openapi_server import util


async def conversation_message_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new ConversationMessage

    Outlines the parameters and data fields used when creating a new ConversationMessage

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Conversation Messages
    :type body: dict | bytes

    """
    body = ConversationMessageCreateRequest.from_dict(body)
    return web.Response(status=200)


async def conversation_message_index(request: web.Request, conversation_id, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, order=None, page_token=None, query=None, updated_since=None) -> web.Response:
    """Return the data for all ConversationMessages

    Outlines the parameters, optional and required, used when requesting the data for all ConversationMessages

    :param conversation_id: The unique identifier for a single Conversation. Use the keyword &#x60;null&#x60; to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property.
    :type conversation_id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter ConversationMessage records to those having the &#x60;created_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter ConversationMessage records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the ConversationMessage records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;body&#x60; matching a given string.
    :type query: str
    :param updated_since: Filter ConversationMessage records to those having the &#x60;updated_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def conversation_message_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ConversationMessage

    Outlines the parameters, optional and required, used when requesting the data for a single ConversationMessage

    :param id: The unique identifier for the ConversationMessage.
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
