import json
from collections.abc import Iterable
from enum import StrEnum
from typing import Any, Callable
from urllib.parse import urljoin

from ors.types import Context, GeoJSON, HTTPClient


def _prepare_headers(headers: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in headers.items() if v is not None}


class Endpoints(StrEnum):
    ISOCHRONES = "isochrones"


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
        url = _prepare_isoch_url(ctx.base_url, Endpoints.ISOCHRONES, ctx.profile)
        print(url)
        resp = http.request(
            "POST",
            url,
            body=_prepare_isoch_body(body),
            headers=_prepare_headers(ctx.headers),
        )
        return _parse_isoch_response(resp.data)

    return call
