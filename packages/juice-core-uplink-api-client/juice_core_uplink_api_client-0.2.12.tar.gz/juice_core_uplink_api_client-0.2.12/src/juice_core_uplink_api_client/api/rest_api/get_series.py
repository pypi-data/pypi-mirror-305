from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.series_data import SeriesData
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["body"] = body

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest_api/series/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list["SeriesData"] | None:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SeriesData.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list["SeriesData"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str,
) -> Response[Any | list["SeriesData"]]:
    """Retrieve a geometry series of a trajectory

     Restricts the returned queries by filtering against a **body** query parameter in the URL.
    The **body** expected value is the JSON string corresponding to the following structure:
    * start: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * end: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * trajectory: the name of the trajectory
    * series: the name of the series to be retrieved

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SeriesData']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: str,
) -> Any | list["SeriesData"] | None:
    """Retrieve a geometry series of a trajectory

     Restricts the returned queries by filtering against a **body** query parameter in the URL.
    The **body** expected value is the JSON string corresponding to the following structure:
    * start: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * end: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * trajectory: the name of the trajectory
    * series: the name of the series to be retrieved

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SeriesData']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str,
) -> Response[Any | list["SeriesData"]]:
    """Retrieve a geometry series of a trajectory

     Restricts the returned queries by filtering against a **body** query parameter in the URL.
    The **body** expected value is the JSON string corresponding to the following structure:
    * start: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * end: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * trajectory: the name of the trajectory
    * series: the name of the series to be retrieved

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SeriesData']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: str,
) -> Any | list["SeriesData"] | None:
    """Retrieve a geometry series of a trajectory

     Restricts the returned queries by filtering against a **body** query parameter in the URL.
    The **body** expected value is the JSON string corresponding to the following structure:
    * start: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * end: the date formatted as ISO8601 in UTC scale (2030-07-05T01:44:47Z)
    * trajectory: the name of the trajectory
    * series: the name of the series to be retrieved

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SeriesData']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
