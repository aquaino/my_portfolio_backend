from flask import Flask
from flask_restful import Api
from app.models import db
from flask_migrate import Migrate

from resources.customer import Customer, CustomerList

migrate = Migrate()
api = Api()


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["FLASK_SECRET_KEY"] = "A super secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["QLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Database
    db.init_app(app)
    migrate.init_app(app, db)

    # API endpoints
    api.add_resource(Customer, '/customers/<int:id>')
    api.add_resource(CustomerList, '/customers')

    api.init_app(app)

    # CLI commands
    from app.commands import init_db_command
    app.cli.add_command(init_db_command)

    return app
