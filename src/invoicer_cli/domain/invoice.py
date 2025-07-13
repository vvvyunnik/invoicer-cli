from datetime import date

from pydantic import BaseModel


class Invoice(BaseModel):
    issue_date: date | None
    issuer: str | None
