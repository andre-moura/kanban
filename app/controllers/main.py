from flask import Blueprint, render_template, request


main = Blueprint('main', __name__)


@main.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')


@main.route('/projects')
def projects():
    if request.method == "GET":
        return render_template('projects.html')


@main.route('/boards')
def project():
    if request.method == "GET":
        return render_template('boards.html')


@main.route('/kanban', methods=['GET', 'POST'])
def board():
    if request.method == 'GET':
        return render_template('kanban.html')
    if request.method == 'POST':
        print(request.get_json())
        return render_template('kanban.html')


@main.route('/members')
def members():
    if request.method == "GET":
        return render_template('members.html')