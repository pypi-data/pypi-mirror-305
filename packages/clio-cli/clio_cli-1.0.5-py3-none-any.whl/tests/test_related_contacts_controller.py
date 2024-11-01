# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.related_contacts_list import RelatedContactsList


pytestmark = pytest.mark.asyncio

async def test_related_contacts_index(client):
    """Test case for related_contacts_index

    Return the related contact data for a single matter
    """
    params = [('fields', 'fields_example'),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/matters/{matter_id}/related_contacts.json'.format(matter_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

