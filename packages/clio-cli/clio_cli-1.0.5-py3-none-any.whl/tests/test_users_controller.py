# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user_list import UserList
from openapi_server.models.user_show import UserShow


pytestmark = pytest.mark.asyncio

async def test_user_index(client):
    """Test case for user_index

    Return the data for all Users
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('enabled', True),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('include_co_counsel', True),
                    ('limit', 56),
                    ('name', 'name_example'),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('pending_setup', True),
                    ('role', 'role_example'),
                    ('subscription_type', 'subscription_type_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_show(client):
    """Test case for user_show

    Return the data for a single User
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
        path='/api/v4/users/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_who_am_i(client):
    """Test case for user_who_am_i

    Return the data for the current User
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
        path='/api/v4/users/who_am_i.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

