from flask import Flask
from .extensions import db
# from flask_sqlalchemy import SQLAlchemy
from .routes import routes
from os import path


# Name of the database
DB_NAME = "database.db"


def create_app():
    """
    Create a new app
    :return: app
    """
    # Create a new app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Add the database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Add routes
    app.register_blueprint(routes, url_prefix="/")

    # Create database
    create_database(app)

    return app


def create_database(app):
    """
    Create a database
    :param app: app
    :return: None
    """
    # If the database does not exist, create it
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database Created")
