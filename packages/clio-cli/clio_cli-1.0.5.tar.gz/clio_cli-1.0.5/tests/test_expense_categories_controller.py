# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.expense_category_create_request import ExpenseCategoryCreateRequest
from openapi_server.models.expense_category_list import ExpenseCategoryList
from openapi_server.models.expense_category_show import ExpenseCategoryShow
from openapi_server.models.expense_category_update_request import ExpenseCategoryUpdateRequest
from openapi_server.models.lauk_expense_category_list import LaukExpenseCategoryList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_category_create(client):
    """Test case for expense_category_create

    Create a new ExpenseCategory
    """
    body = openapi_server.ExpenseCategoryCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/expense_categories.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_category_destroy(client):
    """Test case for expense_category_destroy

    Delete a single ExpenseCategory
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/expense_categories/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_category_index(client):
    """Test case for expense_category_index

    Return the data for all ExpenseCategories
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('entry_type', 'entry_type_example'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/expense_categories.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_category_show(client):
    """Test case for expense_category_show

    Return the data for a single ExpenseCategory
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'if_modified_since': '2013-10-20',
        'if_none_match': 'if_none_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/expense_categories/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_category_update(client):
    """Test case for expense_category_update

    Update a single ExpenseCategory
    """
    body = openapi_server.ExpenseCategoryUpdateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v4/expense_categories/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lauk_expense_category_index(client):
    """Test case for lauk_expense_category_index

    List Expense Categories
    """
    params = [('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('limit', 56),
                    ('name', 'name_example'),
                    ('page_token', 'page_token_example'),
                    ('practice_area', 'practice_area_example'),
                    ('region', 'region_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/lauk_expense_categories.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

