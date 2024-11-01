# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_version_list import DocumentVersionList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_document_version_index(client):
    """Test case for document_version_index

    Return the data for all DocumentVersions
    """
    params = [('fields', 'fields_example'),
                    ('fully_uploaded', True),
                    ('id', 56),
                    ('limit', 56),
                    ('page_token', 'page_token_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/documents/{id}/versions.json'.format(id2=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

