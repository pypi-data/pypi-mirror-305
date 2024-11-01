# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_theme_list import BillThemeList
from openapi_server.models.bill_theme_show import BillThemeShow
from openapi_server.models.bill_theme_update_request import BillThemeUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bill_theme_index(client):
    """Test case for bill_theme_index

    Return the data for all BillThemes
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('page_token', 'page_token_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/bill_themes.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bill_theme_update(client):
    """Test case for bill_theme_update

    Update a single BillTheme
    """
    body = openapi_server.BillThemeUpdateRequest()
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
        path='/api/v4/bill_themes/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

