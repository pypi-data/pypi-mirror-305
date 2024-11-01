# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_contacts_list import MatterContactsList


pytestmark = pytest.mark.asyncio

async def test_matter_contacts_index(client):
    """Test case for matter_contacts_index

    Return the related contact data for a single matter
    """
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example'),
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
        path='/api/v4/matters/{matter_id}/contacts.json'.format(matter_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

