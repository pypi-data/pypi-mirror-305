from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.outstanding_client_balance_list import OutstandingClientBalanceList
from openapi_server import util


async def outstanding_client_balance_index(request: web.Request, x_api_version=None, contact_id=None, fields=None, last_paid_end_date=None, last_paid_start_date=None, limit=None, newest_bill_due_end_date=None, newest_bill_due_start_date=None, originating_attorney_id=None, page_token=None, responsible_attorney_id=None) -> web.Response:
    """Return the data for all OutstandingClientBalances

    Outlines the parameters, optional and required, used when requesting the data for all OutstandingClientBalances

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a OutstandingClientBalance. The list will be filtered to include only the OutstandingClientBalance records with the matching property.
    :type contact_id: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param last_paid_end_date: Filter OutstandingClientBalance records for those whose bills have been paid before the specified date
    :type last_paid_end_date: str
    :param last_paid_start_date: Filter OutstandingClientBalance records for those whose bills have been paid after the specified date
    :type last_paid_start_date: str
    :param limit: A limit on the number of OutstandingClientBalance records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param newest_bill_due_end_date: Filter OutstandingClientBalance records for the contact&#39;s newest bill due date before the specified date
    :type newest_bill_due_end_date: str
    :param newest_bill_due_start_date: Filter OutstandingClientBalance records for the contact&#39;s newest bill due date after the specified date
    :type newest_bill_due_start_date: str
    :param originating_attorney_id: Filters OutstandingClientBalance records to those with matters that have a matching originating attorney.
    :type originating_attorney_id: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param responsible_attorney_id: Filter OutstandingClientBalance records to those with matters that have a matching responsible attorney
    :type responsible_attorney_id: int

    """
    last_paid_end_date = util.deserialize_date(last_paid_end_date)
    last_paid_start_date = util.deserialize_date(last_paid_start_date)
    newest_bill_due_end_date = util.deserialize_date(newest_bill_due_end_date)
    newest_bill_due_start_date = util.deserialize_date(newest_bill_due_start_date)
    return web.Response(status=200)
