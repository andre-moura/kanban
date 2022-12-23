from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user
from app.models.tables import UserProjects, Project, Kanban


main = Blueprint('main', __name__)

@main.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/projects')
@login_required
def projects():
    if request.method == "GET":
        user = current_user
        user_projects = UserProjects.query.filter_by(id_user=user.id).all()

        projects_ids = []
        for user_project in user_projects:
            projects_ids.append(user_project.id)

        projects = Project.query.filter(Project.id.in_(tuple(projects_ids))).all()
        return render_template('projects.html', projects=projects)


@main.route('/boards/<id>')
@login_required
def boards(id):
    if request.method == 'GET':
        kanbans = Kanban.query.filter_by(id_project=id).all()
        return render_template('boards.html', kanbans=kanbans)


@main.route('/kanban/<id>', methods=['GET', 'POST'])
@login_required
def kanban(id):
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