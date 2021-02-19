import click
from flask.cli import with_appcontext
# from datetime import datetime
from werkzeug.security import generate_password_hash

from .models import db
from .models import Users, User_Type, Students, Address, Fees, Notice

@click.command(name="create_tables",help="Create tables main application")
@with_appcontext
def create_tables():
    db.create_all()

    # Initial records in new database

    pw      = "Strongpassword123"
    pw_hash = generate_password_hash(pw, method="sha256")

    user1 = Users(username="administrator", password=pw_hash, email="admin@admin.com", image_file="admin.jpg")
    user2 = Users(username="johndoe", password=pw_hash, email="john.doe@admin.com", image_file="john.jpg")
    user3 = Users(username="janedoe", password=pw_hash, email="jane.doe@admin.com", image_file="jane.jpg")
    db.session.add_all([user1, user2, user3])

    db.session.commit()
    