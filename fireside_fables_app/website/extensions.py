# Created extensions.py to address the circular import error.
from flask_sqlalchemy import SQLAlchemy

# Create a new database
db = SQLAlchemy()
