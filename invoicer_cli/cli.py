import asyncio

import typer

from config.settings import settings
from services.pdf_reader import PdfReader

app = typer.Typer(no_args_is_help=True)


@app.command()
def process():
    asyncio.run(_process_async())


async def _process_async():
    try:
        content = await PdfReader.read(settings.invoices_dir)
        print(content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app()
