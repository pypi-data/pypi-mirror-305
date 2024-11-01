from typing import List, Dict
from aiohttp import web

from openapi_server.models.credit_memo_list import CreditMemoList
from openapi_server.models.credit_memo_show import CreditMemoShow
from openapi_server.models.error import Error
from openapi_server import util


async def credit_memo_index(request: web.Request, x_api_version=None, contact_id=None, created_since=None, fields=None, ids=None, limit=None, order=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all CreditMemos

    Outlines the parameters, optional and required, used when requesting the data for all CreditMemos

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the CreditMemo records with the matching property.
    :type contact_id: int
    :param created_since: Filter CreditMemo records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter CreditMemo records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of CreditMemo records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the CreditMemo records by the given field. Default: &#x60;date(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter CreditMemo records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def credit_memo_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single CreditMemo

    Outlines the parameters, optional and required, used when requesting the data for a single CreditMemo

    :param id: The unique identifier for the CreditMemo.
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
