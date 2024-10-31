import typer

from .export import export

app = typer.Typer()
app.command()(export)


if __name__ == "__main__":
    app()