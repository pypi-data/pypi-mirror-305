# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.report_create_request import ReportCreateRequest
from openapi_server.models.report_list import ReportList
from openapi_server.models.report_show import ReportShow


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_report_create(client):
    """Test case for report_create

    Create a new Report
    """
    body = openapi_server.ReportCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/reports.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_download(client):
    """Test case for report_download

    Download the completed Report
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/reports/{id}/download.json'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_index(client):
    """Test case for report_index

    Return the data for all Reports
    """
    params = [('category', 'category_example'),
                    ('created_before', '2013-10-20T19:20:30+01:00'),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('kind', 'kind_example'),
                    ('limit', 56),
                    ('output_format', 'output_format_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('source', 'source_example'),
                    ('state', 'state_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/reports.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_show(client):
    """Test case for report_show

    Return the data for a single Report
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
        path='/api/v4/reports/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

