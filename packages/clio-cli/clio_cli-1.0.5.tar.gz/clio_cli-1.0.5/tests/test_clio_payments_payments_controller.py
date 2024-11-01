# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clio_payments_payment_list import ClioPaymentsPaymentList
from openapi_server.models.clio_payments_payment_show import ClioPaymentsPaymentShow
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_clio_payments_payment_index(client):
    """Test case for clio_payments_payment_index

    Return the data for all ClioPaymentsPayments
    """
    params = [('bill_id', 56),
                    ('contact_id', 56),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('page_token', 'page_token_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/clio_payments/payments.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clio_payments_payment_show(client):
    """Test case for clio_payments_payment_show

    Return the data for a single ClioPaymentsPayment
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
        path='/api/v4/clio_payments/payments/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

