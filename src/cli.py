import asyncio
import typer

from config.settings import Settings

app = typer.Typer(no_args_is_help=True)


@app.command()
def process():
    settings = Settings()
    asyncio.run(_process_async(settings))


async def _process_async(settings: Settings):
    print("starting invoicer-cli")
    print(settings.invoices_dir)


if __name__ == "__main__":
    app()
