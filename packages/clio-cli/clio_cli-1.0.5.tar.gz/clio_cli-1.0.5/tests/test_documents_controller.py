# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_copy_request import DocumentCopyRequest
from openapi_server.models.document_create_request import DocumentCreateRequest
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_show import DocumentShow
from openapi_server.models.document_update_request import DocumentUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_document_copy(client):
    """Test case for document_copy

    Copy a Document
    """
    body = openapi_server.DocumentCopyRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/documents/{id}/copy.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_document_create(client):
    """Test case for document_create

    Create a new Document
    """
    body = openapi_server.DocumentCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/documents.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_destroy(client):
    """Test case for document_destroy

    Delete a single Document
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/documents/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_download(client):
    """Test case for document_download

    Download the Document
    """
    params = [('document_version_id', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/documents/{id}/download.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_index(client):
    """Test case for document_index

    Return the data for all Documents
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
        path='/api/v4/documents.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_show(client):
    """Test case for document_show

    Return the data for a single Document
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
        path='/api/v4/documents/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_document_update(client):
    """Test case for document_update

    Update a single Document
    """
    body = openapi_server.DocumentUpdateRequest()
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
        path='/api/v4/documents/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

