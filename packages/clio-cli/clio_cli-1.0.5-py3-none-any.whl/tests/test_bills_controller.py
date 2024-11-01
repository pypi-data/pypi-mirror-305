# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_list import BillList
from openapi_server.models.bill_show import BillShow
from openapi_server.models.bill_update_request import BillUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bill_destroy(client):
    """Test case for bill_destroy

    Delete or void a Bill
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/bills/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_index(client):
    """Test case for bill_index

    Return the data for all Bills
    """
    params = [('client_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('due_after', '2013-10-20'),
                    ('due_at', '2013-10-20'),
                    ('due_before', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('issued_after', '2013-10-20'),
                    ('issued_before', '2013-10-20'),
                    ('last_sent_end_date', '2013-10-20'),
                    ('last_sent_start_date', '2013-10-20'),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('order', 'order_example'),
                    ('originating_attorney_id', 56),
                    ('overdue_only', True),
                    ('page_token', 'page_token_example'),
                    ('query', 56),
                    ('responsible_attorney_id', 56),
                    ('state', 'state_example'),
                    ('status', 'status_example'),
                    ('type', 'type_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/bills.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_preview(client):
    """Test case for bill_preview

    Returns the pre-rendered html for the Bill
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/bills/{id}/preview.json'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_show(client):
    """Test case for bill_show

    Return the data for a single Bill
    """
    params = [('fields', 'fields_example'),
                    ('navigation.next', 56),
                    ('navigation.previous', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'if_modified_since': '2013-10-20',
        'if_none_match': 'if_none_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/bills/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bill_update(client):
    """Test case for bill_update

    Update a single Bill
    """
    body = openapi_server.BillUpdateRequest()
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
        path='/api/v4/bills/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

