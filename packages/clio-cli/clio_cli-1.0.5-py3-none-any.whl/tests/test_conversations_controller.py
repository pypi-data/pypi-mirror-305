# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_list import ConversationList
from openapi_server.models.conversation_show import ConversationShow
from openapi_server.models.conversation_update_request import ConversationUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_conversation_index(client):
    """Test case for conversation_index

    Return the data for all Conversations
    """
    params = [('archived', True),
                    ('contact_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('date', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('for_user', True),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('read_status', True),
                    ('time_entries', True),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/conversations.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversation_show(client):
    """Test case for conversation_show

    Return the data for a single Conversation
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
        path='/api/v4/conversations/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversation_update(client):
    """Test case for conversation_update

    Update a single Conversation
    """
    body = openapi_server.ConversationUpdateRequest()
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
        path='/api/v4/conversations/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

