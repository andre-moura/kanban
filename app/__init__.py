from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import jyserver.Flask as jsf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SECRET_KEY'] = '65a19a98-e2d1-4bfa-98bf-a8feec4ec0ed'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
from app.controllers import logged_view
from app.models import tables

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=tables.User
    )