# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.utbms_code_list import UtbmsCodeList
from openapi_server.models.utbms_code_show import UtbmsCodeShow


pytestmark = pytest.mark.asyncio

async def test_utbms_code_index(client):
    """Test case for utbms_code_index

    Return the data for all UtbmsCodes
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('type', 'type_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00'),
                    ('utbms_set_id', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/utbms/codes.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_utbms_code_show(client):
    """Test case for utbms_code_show

    Return the data for a single UtbmsCode
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
        path='/api/v4/utbms/codes/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

