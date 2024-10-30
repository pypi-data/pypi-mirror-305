import json
from collections.abc import Iterable
from typing import Any, Callable
from urllib.parse import urljoin

import urllib3

from ors.client import JSON, Context, GeoJSON, HTTPClient
from ors.exceptions import FailedRequest, HTTPError


def _prepare_headers(headers: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in headers.items() if v is not None}


def _prepare_isoch_url(base: str, endpoint: str, profile: str) -> str:
    ep = endpoint + "/" + profile
    return urljoin(base=base, url=ep)


def _parse_isoch_response(resp: str) -> GeoJSON:
    return json.loads(resp)


def _prepare_isoch_body(body: dict[str, Any]) -> str:
    return json.dumps({k: v for k, v in body.items() if v is not None})


def isochrones(
    locations: Iterable[tuple[float, float]],
    range_: Iterable[int],
    attributes: Iterable[str] | None = None,
    id_: str | None = None,
    intersections: bool | None = None,
    interval: int | None = None,
    location_type: str | None = None,
    options: dict[Any, Any] | None = None,
    range_type: str | None = None,
    smoothing: int | None = None,
    area_units: str | None = None,
    units: str | None = None,
    profile: str = "driving-car",
) -> Callable[[HTTPClient, Context], GeoJSON]:
    body = {
        "locations": locations,
        "range": range_,
        "attributes": attributes,
        "id": id_,
        "intersections": intersections,
        "interval": interval,
        "location_type": location_type,
        "options": options,
        "range_type": range_type,
        "smoothing": smoothing,
        "area_units": area_units,
        "units": units,
    }

    def call(http: HTTPClient, ctx: Context) -> GeoJSON:
        url = _prepare_isoch_url(ctx.base_url, ctx.endpoints.ISOCHRONES, profile)
        try:
            resp = http.request(
                "POST",
                url,
                body=_prepare_isoch_body(body),
                headers=_prepare_headers(ctx.headers),
            )
        except urllib3.exceptions.HTTPError as e:
            raise HTTPError(f"request failed on isochrones endpoint: {e}")
        if resp.status != 200:
            raise FailedRequest(f"request returned a failed status: {resp.status} with message {resp.data}")
        return _parse_isoch_response(resp.data)

    return call


def health() -> Callable[[HTTPClient, Context], JSON]:
    def call(http: HTTPClient, ctx: Context) -> JSON:
        url = urljoin(base=ctx.base_url, url=ctx.endpoints.HEALTH)
        try:
            resp = http.request(
                "GET",
                url,
            )
        except urllib3.exceptions.HTTPError as e:
            raise HTTPError(f"request failed: {e} when accessing {url}")
        if resp.status != 200:
            raise FailedRequest(f"request on {url} returned a failed status: {resp.status} with message {resp.data}")
        return json.loads(resp.data)

    return call
