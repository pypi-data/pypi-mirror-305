from typing import List, Dict
from aiohttp import web

from openapi_server.models.clio_payments_payment_list import ClioPaymentsPaymentList
from openapi_server.models.clio_payments_payment_show import ClioPaymentsPaymentShow
from openapi_server.models.error import Error
from openapi_server import util


async def clio_payments_payment_index(request: web.Request, x_api_version=None, bill_id=None, contact_id=None, fields=None, ids=None, limit=None, page_token=None, state=None) -> web.Response:
    """Return the data for all ClioPaymentsPayments

    Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsPayments

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param bill_id: Filter ClioPaymentsPayment records to those that are allocated to the specified bill.
    :type bill_id: int
    :param contact_id: Filter ClioPaymentsPayment records to those that are assigned to the specified contact.
    :type contact_id: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter ClioPaymentsPayment records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param state: Filter ClioPaymentsPayment records to those in a given state.
    :type state: str

    """
    return web.Response(status=200)


async def clio_payments_payment_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ClioPaymentsPayment

    Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsPayment

    :param id: The unique identifier for the ClioPaymentsPayment.
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
