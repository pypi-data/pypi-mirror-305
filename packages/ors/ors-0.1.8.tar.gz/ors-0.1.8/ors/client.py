from dataclasses import asdict
from typing import Callable

from urllib3 import PoolManager

from ors.types import Context, Endpoint, HTTPClient, Response, default_headers


def context(
    base_url: str = "https://api.openrouteservice.org/v2/",
    auth: str | None = None,
) -> Context:
    headers = default_headers()
    headers["Authorization"] = auth
    return Context(base_url, headers)


def client(
    ctx: Context = context(),
    http: HTTPClient = PoolManager(),
) -> Callable[[Endpoint], Response]:
    def _(
        endpoint: Endpoint,
    ) -> Response:
        return endpoint(http, ctx)

    return _
