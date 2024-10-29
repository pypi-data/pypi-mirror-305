from dataclasses import asdict
from typing import Callable
from ors.types import Endpoint, HTTPClient, Response, Context, default_headers
from urllib3 import PoolManager


def context(
    base_url: str = "https://api.openrouteservice.org/v2",
    auth: str | None = None,
    profile: str = "driving-car",
) -> Context:
    headers = default_headers()
    headers["Authorization"] = auth
    return Context(base_url, headers, profile)


def set_context(**kwargs) -> Callable[[Context], Context]:
    def _(ctx: Context) -> Context:
        for k, v in kwargs.items():
            setattr(ctx, k, v)
        return ctx

    return _


def override_context(**kwargs) -> Callable[[Context], Context]:
    def _(ctx: Context) -> Context:
        ctx_dict = asdict(ctx)
        ctx_dict.update(kwargs)
        return Context(**ctx_dict)

    return _


ContextOverride = Callable[[Context], Context]


def client(
    ctx: Context = context(),
    http: HTTPClient = PoolManager(),
) -> Callable[[Endpoint, ContextOverride | None], Response]:
    def _(
        endpoint: Endpoint,
        context_override: ContextOverride | None = None,
    ) -> Response:
        if context_override:
            return endpoint(http, context_override(ctx))
        return endpoint(http, ctx)

    return _
