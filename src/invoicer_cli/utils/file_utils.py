import json
from typing import Any


class FileUtils:
    @staticmethod
    def load_json(path: str) -> dict[str, Any]:
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Failed to load JSON from {path}: {e}")
            raise
