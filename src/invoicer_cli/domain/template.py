import re

from pydantic import BaseModel
from typing import List, Pattern, Union, Self

from invoicer_cli.utils.file_utils import FileUtils


class Field(BaseModel):
    name: str
    type: str
    pattern: Pattern[str]

    @classmethod
    def _compile_pattern(cls, v: Union[str, Pattern[str]]) -> Pattern[str]:
        if isinstance(v, Pattern):
            return v
        if isinstance(v, str):
            try:
                return re.compile(v)
            except re.error as e:
                raise ValueError(f"Invalid regex for field pattern: {e}")
        raise TypeError(f"Pattern must be str or Pattern, got {type(v)}")


class Template(BaseModel):
    fields: List[Field]

    @classmethod
    def from_file(cls, path: str) -> Self:
        raw = FileUtils.load_json(path)
        return cls(fields=raw.get("fields", []))
