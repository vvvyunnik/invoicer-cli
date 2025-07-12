import asyncio
from pathlib import Path
from typing import Any
import pdfplumber


class PdfReader:
    @staticmethod
    async def read(file_path: str) -> dict[str, Any]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not path.is_file():
            raise IsADirectoryError(f"Expected a file but got a directory: {file_path}")

        try:
            result = await asyncio.to_thread(_read, path)
        except FileNotFoundError:
            raise
        except Exception as exc:
            print(f"Error reading PDF {file_path}: {exc}")
            raise RuntimeError(f"Failed to read PDF: {exc}") from exc
        if not result["text"].strip():
            raise ValueError(f"No text could be extracted from: {file_path}")

        return result


def _read(path: Path) -> dict[str, Any]:
    with pdfplumber.open(path) as pdf:
        num_pages = len(pdf.pages)
        if num_pages != 1:
            raise ValueError(
                f"Expected a single-page PDF, but got {num_pages} pages: {path}"
            )
        text = pdf.pages[0].extract_text() or ""
    return {"file_path": str(path), "text": text}
