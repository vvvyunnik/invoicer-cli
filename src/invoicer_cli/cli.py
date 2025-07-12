import asyncio

import typer

from config.settings import settings
from invoicer_cli.services.extractor import Extractor

app = typer.Typer(no_args_is_help=True)


@app.command()
def process():
    asyncio.run(_process_async())


async def _process_async():
    try:
        extracted_pdf = await Extractor.extract(settings.invoices_dir)
        print(extracted_pdf)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app()
