from flask import Flask, render_template, request


app = Flask(__name__)


from app.controllers import views
from app.controllers import logged_view