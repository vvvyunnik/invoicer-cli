from pydantic import BaseModel
from typing import List


class FieldTemplate(BaseModel):
    name: str
    pattern: str


class InvoiceTemplate(BaseModel):
    fields: List[FieldTemplate]
