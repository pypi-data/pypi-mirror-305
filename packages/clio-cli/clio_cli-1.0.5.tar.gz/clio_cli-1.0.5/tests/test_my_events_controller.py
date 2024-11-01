# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.my_event_list import MyEventList
from openapi_server.models.my_event_show import MyEventShow
from openapi_server.models.my_event_update_request import MyEventUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_my_event_destroy(client):
    """Test case for my_event_destroy

    Clear (delete) a single in-app notification event
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/internal_notifications/my_events/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_event_index(client):
    """Test case for my_event_index

    Return the data for all of my in-app notification events
    """
    params = [('fields', 'fields_example'),
                    ('limit', 56),
                    ('page_token', 'page_token_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/internal_notifications/my_events.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_my_event_update(client):
    """Test case for my_event_update

    Mark a single in-app notification event as read/unread
    """
    body = openapi_server.MyEventUpdateRequest()
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
        path='/api/v4/internal_notifications/my_events/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

