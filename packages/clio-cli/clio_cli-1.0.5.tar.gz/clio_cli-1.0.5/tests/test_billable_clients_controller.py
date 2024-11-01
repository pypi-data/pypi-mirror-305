# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billable_client_list import BillableClientList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_billable_client_index(client):
    """Test case for billable_client_index

    Return the data for all BillableClients
    """
    params = [('client_id', 56),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('end_date', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('originating_attorney_id', 56),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('responsible_attorney_id', 56),
                    ('start_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/billable_clients.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

