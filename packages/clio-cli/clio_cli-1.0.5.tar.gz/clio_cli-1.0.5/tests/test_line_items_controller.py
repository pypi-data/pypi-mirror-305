# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.line_item_list import LineItemList
from openapi_server.models.line_item_show import LineItemShow
from openapi_server.models.line_item_update_request import LineItemUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_line_item_destroy(client):
    """Test case for line_item_destroy

    Delete a single LineItem
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/line_items/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_item_index(client):
    """Test case for line_item_index

    Return the data for all LineItems
    """
    params = [('activity_id', 56),
                    ('bill_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('display', True),
                    ('exclude_ids[]', 56),
                    ('fields', 'fields_example'),
                    ('group_ordering', 56),
                    ('ids[]', 56),
                    ('kind', 'kind_example'),
                    ('limit', 56),
                    ('matter_id', 56),
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
        path='/api/v4/line_items.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_line_item_update(client):
    """Test case for line_item_update

    Update a single LineItem
    """
    body = openapi_server.LineItemUpdateRequest()
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
        path='/api/v4/line_items/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

