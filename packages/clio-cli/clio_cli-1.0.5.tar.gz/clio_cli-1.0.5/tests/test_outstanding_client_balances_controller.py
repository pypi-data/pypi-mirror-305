# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.outstanding_client_balance_list import OutstandingClientBalanceList


pytestmark = pytest.mark.asyncio

async def test_outstanding_client_balance_index(client):
    """Test case for outstanding_client_balance_index

    Return the data for all OutstandingClientBalances
    """
    params = [('contact_id', 56),
                    ('fields', 'fields_example'),
                    ('last_paid_end_date', '2013-10-20'),
                    ('last_paid_start_date', '2013-10-20'),
                    ('limit', 56),
                    ('newest_bill_due_end_date', '2013-10-20'),
                    ('newest_bill_due_start_date', '2013-10-20'),
                    ('originating_attorney_id', 56),
                    ('page_token', 'page_token_example'),
                    ('responsible_attorney_id', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/outstanding_client_balances.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

