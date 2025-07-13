from datetime import date, datetime
from typing import Any, Callable


def to_string(raw: str) -> str:
    return raw


def to_date(raw: str) -> date:
    return datetime.strptime(raw, "%d-%m-%Y").date()


CONVERTERS: dict[str, Callable[[str], Any]] = {
    "string": to_string,
    "date": to_date,
}
