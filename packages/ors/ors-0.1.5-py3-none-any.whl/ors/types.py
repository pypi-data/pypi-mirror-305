from dataclasses import dataclass, field
from typing import Any, Callable

from urllib3 import PoolManager


def default_headers() -> dict[str, str]:
    d = {
        "Accept": "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
        "Content-Type": "application/json; charset=utf-8",
    }
    return d


@dataclass
class Context:
    base_url: str = "https://api.openrouteservice.org/v2/"
    headers: dict[str, str] = field(default_factory=default_headers)
    profile: str = "driving-car"


GeoJSON = dict[str, Any]
JSON = dict[str, Any]
Response = GeoJSON | JSON
HTTPClient = PoolManager
Endpoint = Callable[[HTTPClient, Context], GeoJSON]
