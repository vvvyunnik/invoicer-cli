from invoicer_cli.config.settings import settings
from invoicer_cli.domain.invoice import Invoice
from invoicer_cli.services.pdf_reader import PdfReader

from invoicer_cli.domain.template import Field, Template
from invoicer_cli.utils.converters import CONVERTERS


class Extractor:
    @staticmethod
    async def extract(pdf_path: str) -> Invoice:
        text = await PdfReader.read(pdf_path)

        if not text:
            raise ValueError(f"File is empty: {pdf_path}")

        template = Template.from_file(settings.template_path)

        data = {
            field.name: Extractor._parse_field(field, text) for field in template.fields
        }

        return Invoice(**data)

    @staticmethod
    def _parse_field(field: Field, text: str):
        if not field.name or not field.pattern:
            print("Skipping bad template item: %r", field)
            return None

        match = field.pattern.search(text)
        if not match:
            print("Field %s not found in file", field.name)
            return None

        raw = match.group(1).strip()
        converter = CONVERTERS.get(field.type, CONVERTERS["string"])
        try:
            return converter(raw)
        except Exception as e:
            print("Error converting field %s: raw=%r, error=%s", field.name, raw, e)
            return None
