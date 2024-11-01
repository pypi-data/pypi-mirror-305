# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.folder_create_request import FolderCreateRequest
from openapi_server.models.folder_list import FolderList
from openapi_server.models.folder_show import FolderShow
from openapi_server.models.folder_update_request import FolderUpdateRequest
from openapi_server.models.item_list import ItemList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_folder_create(client):
    """Test case for folder_create

    Create a new Folder
    """
    body = openapi_server.FolderCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/folders.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_folder_destroy(client):
    """Test case for folder_destroy

    Delete a single Folder
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/folders/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_folder_index(client):
    """Test case for folder_index

    Return the data for all Folders
    """
    params = [('contact_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('document_category_id', 56),
                    ('external_property_name', 'external_property_name_example'),
                    ('external_property_value', 'external_property_value_example'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('include_deleted', True),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('parent_id', 56),
                    ('query', 'query_example'),
                    ('scope', 'scope_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/folders.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_folder_list(client):
    """Test case for folder_list

    Return the data of the contents of a Folder
    """
    params = [('contact_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('document_category_id', 56),
                    ('external_property_name', 'external_property_name_example'),
                    ('external_property_value', 'external_property_value_example'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('include_deleted', True),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('parent_id', 56),
                    ('query', 'query_example'),
                    ('scope', 'scope_example'),
                    ('show_uncompleted', True),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/folders/list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_folder_show(client):
    """Test case for folder_show

    Return the data for a single Folder
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
        path='/api/v4/folders/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_folder_update(client):
    """Test case for folder_update

    Update a single Folder
    """
    body = openapi_server.FolderUpdateRequest()
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
        path='/api/v4/folders/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

