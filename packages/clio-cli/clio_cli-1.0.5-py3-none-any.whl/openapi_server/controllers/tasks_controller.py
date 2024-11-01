from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_list import TaskList
from openapi_server.models.task_show import TaskShow
from openapi_server.models.task_update_request import TaskUpdateRequest
from openapi_server import util


async def task_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Task

    Outlines the parameters and data fields used when creating a new Task

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Tasks
    :type body: dict | bytes

    """
    body = TaskCreateRequest.from_dict(body)
    return web.Response(status=200)


async def task_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Task

    Outlines the parameters, optional and required, used when deleting the record for a single Task

    :param id: The unique identifier for the Task.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def task_index(request: web.Request, x_api_version=None, assignee_id=None, assignee_type=None, assigner_id=None, cascading_source_id=None, client_id=None, complete=None, created_since=None, due_at_from=None, due_at_present=None, due_at_to=None, fields=None, ids=None, limit=None, matter_id=None, order=None, page_token=None, permission=None, priority=None, query=None, responsible_attorney_id=None, status=None, statuses=None, statute_of_limitations=None, task_type_id=None, time_entries_present=None, updated_since=None) -> web.Response:
    """Return the data for all Tasks

    Outlines the parameters, optional and required, used when requesting the data for all Tasks

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param assignee_id: The unique identifier for a single User or Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.
    :type assignee_id: int
    :param assignee_type: Filter Task records to those with a specific assignee. Must be passed if filtering by assignee.
    :type assignee_type: str
    :param assigner_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.
    :type assigner_id: int
    :param cascading_source_id: Filter Task records to those with a parent task that has the specified ID.
    :type cascading_source_id: int
    :param client_id: The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.
    :type client_id: int
    :param complete: Filter Task records to those which are complete or not.
    :type complete: bool
    :param created_since: Filter Task records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param due_at_from: Start of date range when querying by due_at in a range. (Expects an ISO-8601 date).
    :type due_at_from: str
    :param due_at_present: Filter Task records to those that have a due date specified, or not.
    :type due_at_present: bool
    :param due_at_to: End of date range when querying by due_at in a range. (Expects an ISO-8601 date).
    :type due_at_to: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Task records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Task records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.
    :type matter_id: int
    :param order: Orders the Task records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param permission: Filter Task records to those with the given permission. Returns all tasks by default.
    :type permission: str
    :param priority: Filter Task records to those with the given priority.
    :type priority: str
    :param query: Wildcard search for &#x60;name&#x60; or &#x60;description&#x60; matching a given string.
    :type query: str
    :param responsible_attorney_id: Filter Task records to those that have an associated matter with a responsible attorney ID.
    :type responsible_attorney_id: int
    :param status: Filter Task records to those with the given status. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;.
    :type status: str
    :param statuses: Filter Task records to those with the given statuses. Users without advanced tasks enabled may only specify &#39;complete&#39; or &#39;pending&#39;.
    :type statuses: str
    :param statute_of_limitations: Filter Task records to those which are a statute of limitations or not.
    :type statute_of_limitations: bool
    :param task_type_id: The unique identifier for a single TaskType. Use the keyword &#x60;null&#x60; to match those without a Task. The list will be filtered to include only the Task records with the matching property.
    :type task_type_id: int
    :param time_entries_present: Filter Task records to those that have associated time entries, or not.
    :type time_entries_present: bool
    :param updated_since: Filter Task records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    due_at_from = util.deserialize_date(due_at_from)
    due_at_to = util.deserialize_date(due_at_to)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def task_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Task

    Outlines the parameters, optional and required, used when requesting the data for a single Task

    :param id: The unique identifier for the Task.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def task_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Task

    Outlines the parameters and data fields used when updating a single Task

    :param id: The unique identifier for the Task.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Tasks
    :type body: dict | bytes

    """
    body = TaskUpdateRequest.from_dict(body)
    return web.Response(status=200)
