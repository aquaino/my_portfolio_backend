from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from resources.customer import Customer, CustomerList


db = SQLAlchemy()
migrate = Migrate()
api = Api()


def create_app():
    app = Flask(__name__)

    app.config["FLASK_SECRET_KEY"] = "A super secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["QLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Endpoints
    api.add_resource(Customer, '/customers/<int:id>')
    api.add_resource(CustomerList, '/customers')


    api.init_app(app)

    return app
