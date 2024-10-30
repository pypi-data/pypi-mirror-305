from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Callable

from urllib3 import PoolManager

EndpointsEnum = StrEnum


class Endpoints(EndpointsEnum):
    ISOCHRONES = "isochrones"
    HEALTH = "health"


def default_headers() -> dict[str, str]:
    d = {
        "Accept": "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
        "Content-Type": "application/json; charset=utf-8",
    }
    return d


@dataclass(frozen=True)
class Context:
    base_url: str = "https://api.openrouteservice.org/v2/"
    headers: dict[str, str] = field(default_factory=default_headers)
    endpoints: EndpointsEnum = Endpoints


def context(
    base_url: str = "https://api.openrouteservice.org/v2/",
    api_key: str | None = None,
    endpoints: EndpointsEnum = Endpoints,
) -> Context:
    if base_url[-1] != "/":
        base_url = base_url + "/"
    headers = default_headers()
    headers["Authorization"] = api_key
    return Context(base_url, headers, endpoints)


HTTPClient = PoolManager
GeoJSON = dict[str, Any]
JSON = dict[str, Any]
Response = GeoJSON | JSON
Endpoint = Callable[[HTTPClient, Context], Response]


def client(
    ctx: Context = context(),
    http: HTTPClient = PoolManager(),
) -> Callable[[Endpoint], Response]:
    def _(
        endpoint: Endpoint,
    ) -> Response:
        return endpoint(http, ctx)

    return _
