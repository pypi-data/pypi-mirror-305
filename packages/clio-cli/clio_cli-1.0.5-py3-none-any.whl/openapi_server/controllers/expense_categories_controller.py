from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.expense_category_create_request import ExpenseCategoryCreateRequest
from openapi_server.models.expense_category_list import ExpenseCategoryList
from openapi_server.models.expense_category_show import ExpenseCategoryShow
from openapi_server.models.expense_category_update_request import ExpenseCategoryUpdateRequest
from openapi_server.models.lauk_expense_category_list import LaukExpenseCategoryList
from openapi_server import util


async def expense_category_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new ExpenseCategory

    Outlines the parameters and data fields used when creating a new ExpenseCategory

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Expense Categories
    :type body: dict | bytes

    """
    body = ExpenseCategoryCreateRequest.from_dict(body)
    return web.Response(status=200)


async def expense_category_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single ExpenseCategory

    Outlines the parameters, optional and required, used when deleting the record for a single ExpenseCategory

    :param id: The unique identifier for the ExpenseCategory.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def expense_category_index(request: web.Request, x_api_version=None, created_since=None, entry_type=None, fields=None, limit=None, order=None, page_token=None, query=None, updated_since=None) -> web.Response:
    """Return the data for all ExpenseCategories

    Outlines the parameters, optional and required, used when requesting the data for all ExpenseCategories

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter ExpenseCategory records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param entry_type: Filter ExpenseCategory records to those that match the given type.
    :type entry_type: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param limit: A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the ExpenseCategory records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Allows matching search on expense category name.
    :type query: str
    :param updated_since: Filter ExpenseCategory records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def expense_category_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single ExpenseCategory

    Outlines the parameters, optional and required, used when requesting the data for a single ExpenseCategory

    :param id: The unique identifier for the ExpenseCategory.
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


async def expense_category_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single ExpenseCategory

    Outlines the parameters and data fields used when updating a single ExpenseCategory

    :param id: The unique identifier for the ExpenseCategory.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Expense Categories
    :type body: dict | bytes

    """
    body = ExpenseCategoryUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def lauk_expense_category_index(request: web.Request, region, x_api_version=None, fields=None, key=None, limit=None, name=None, page_token=None, practice_area=None) -> web.Response:
    """List Expense Categories

    Outlines the parameters, optional and required, used when requesting the data for all LaukExpenseCategories

    :param region: Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate.
    :type region: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param key: Filter by key.
    :type key: str
    :param limit: A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param name: Filter by expense name.
    :type name: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param practice_area: Filter by expense practice area.
    :type practice_area: str

    """
    return web.Response(status=200)
