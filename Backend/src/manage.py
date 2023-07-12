import pytest
import click

from app import create_app
from app.utils.db import db

app = create_app()
db.init_app(app)
with app.app_context():
    db.create_all()

@click.group()
def cli():
    """Management script for the Flask application."""

@cli.command()
def run():
    print("Running the Flask application...")
    """Run the Flask application."""
    app.run(debug=True)

@cli.command
def test():
    """Run the unit tests."""
    pytest.main(['test'])

if __name__ == '__main__':
    cli()