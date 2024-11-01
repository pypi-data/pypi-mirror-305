# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_create_request import ContactCreateRequest
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_show import ContactShow
from openapi_server.models.contact_update_request import ContactUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_contact_create(client):
    """Test case for contact_create

    Create a new Contact
    """
    body = openapi_server.ContactCreateRequest()
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/contacts.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_destroy(client):
    """Test case for contact_destroy

    Delete a single Contact
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/contacts/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_index(client):
    """Test case for contact_index

    Return the data for all Contacts
    """
    params = [('client_only', True),
                    ('clio_connect_only', True),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('custom_field_ids[]', 56),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('email_only', True),
                    ('exclude_ids[]', 56),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('initial', 'initial_example'),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('shared_resource_id', 56),
                    ('type', 'type_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/contacts.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_show(client):
    """Test case for contact_show

    Return the data for a single Contact
    """
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'if_modified_since': '2013-10-20',
        'if_none_match': 'if_none_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/contacts/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_contact_update(client):
    """Test case for contact_update

    Update a single Contact
    """
    body = openapi_server.ContactUpdateRequest()
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v4/contacts/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

