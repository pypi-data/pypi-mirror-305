# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_transfer_show import BankTransferShow
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bank_transfer_show(client):
    """Test case for bank_transfer_show

    Return the data for a single BankTransfer
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
        path='/api/v4/bank_transfers/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

