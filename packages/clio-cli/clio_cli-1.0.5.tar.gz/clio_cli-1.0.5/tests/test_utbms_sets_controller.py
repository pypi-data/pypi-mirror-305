# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.utbms_set_list import UtbmsSetList


pytestmark = pytest.mark.asyncio

async def test_utbms_set_index(client):
    """Test case for utbms_set_index

    Return the data for all the utbms sets
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/utbms/sets.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

