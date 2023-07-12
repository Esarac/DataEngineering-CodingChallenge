import pytest
import click

from app import create_app
from app.utils.db import db

@click.group()
def cli():
    """Management script for the Flask application."""

@cli.command()
def run():
    """Run the Flask application."""
    app = create_app()
    app.run(debug=True)

@cli.command
def test():
    """Run the unit tests."""
    pytest.main(['tests'])

if __name__ == '__main__':
    cli()