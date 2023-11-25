from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import routes

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Creating a new app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Adding the database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    # Adding routes
    app.register_blueprint(routes, url_prefix="/")
    return app
