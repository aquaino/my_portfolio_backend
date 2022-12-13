import click
from flask.cli import with_appcontext
from app import db


@click.command("init_db")
@with_appcontext
def init_db_command():
    """Create and initialize app database."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database initialized.")
