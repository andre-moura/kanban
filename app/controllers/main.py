from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.models.tables import UserProjects, Project


main = Blueprint('main', __name__)

@main.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/projects')
@login_required
def projects():
    if request.method == "GET":
        # user = current_user
        # projects = ProjectUser.select()
        # print(projects)
        return render_template('projects.html')


@main.route('/boards')
@login_required
def project():
    if request.method == "GET":
        return render_template('boards.html')


@main.route('/kanban', methods=['GET', 'POST'])
@login_required
def board():
    if request.method == 'GET':
        return render_template('kanban.html')
    if request.method == 'POST':
        print(request.get_json())
        return render_template('kanban.html')


@main.route('/members')
@login_required
def members():
    if request.method == "GET":
        return render_template('members.html')