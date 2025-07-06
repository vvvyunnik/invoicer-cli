import asyncio
import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def process():
    asyncio.run(_process_async())


async def _process_async():
    print("starting invoicer-cli")


if __name__ == "__main__":
    app()
