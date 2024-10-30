from __future__ import annotations

import yaml
from typing import Any

from pydantic import BaseModel


class SentryConfig(BaseModel):
    dsn: str
    # Set traces_sample_rate to 1.0 to capture 100%
    sample_rate: float = 0.5
    # We recommend adjusting this value in production.
    profiles_sample_rate: float = 0.2

    traces_sample_rate: float = 1.0

    environment: str
    debug: bool = False
    # enable_tracing: bool = True

    @classmethod
    def from_json(cls, data: str | dict[str, Any]) -> SentryConfig:
        if isinstance(data, str):
            # parsed_data: dict[str, Any] = json.loads(data)
            parsed_data: dict[str, Any] = yaml.load(data, Loader=yaml.FullLoader)
        else:
            parsed_data = data
        return SentryConfig(**parsed_data)


def sentry_setup(config: SentryConfig) -> None:
    import sentry_sdk
    print(config.model_dump())

    sentry_sdk.init(
        **config.model_dump(),
        before_send_transaction=_filter_transactions,
    )


def _filter_transactions(event: Any, _hint: Any) -> Any:
    transaction_path = event.get("transaction") or event.get("request", {}).get("url", "")
    if any(path in transaction_path for path in ("/healthcheck", "/health_check")):
        return None

    if not transaction_path.startswith("/api"):
        return None

    return event
