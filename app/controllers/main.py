from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user
from app.models.tables import UserProjects, Project, Kanban, KanbanList, Task


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

    if request.method == 'POST':
        pass

@main.route('/task', methods=['POST'])
@login_required
def task():
    if request.method == 'POST':
        pass

@main.route('/boards/<id>')
@login_required
def boards(id):
    if request.method == 'GET':
        kanbans = Kanban.query.filter_by(id_project=id).all()
        return render_template('boards.html', kanbans=kanbans)
    

@main.route('/boards', methods=['POST'])
@login_required
def create_board():
    if request.method == 'POST':
        pass


@main.route('/list', methods=['POST'])
@login_required
def list():
    if request.method == 'POST':
        pass

@main.route('/kanban/<id>', methods=['GET', 'POST'])
@login_required
def kanban(id):
    if request.method == 'GET':
        kanban_lists = KanbanList.query.filter_by(id_kanban=id).order_by(KanbanList.order).all()
        ids_lists = []
        for kanban_list in kanban_lists:
            ids_lists.append(kanban_list.id)
        tasks = Task.query.filter(Task.id_list.in_(tuple(ids_lists))).all()
        return render_template('kanban.html', kanban_lists=kanban_lists, tasks=tasks)
        
    if request.method == 'POST':
        return render_template('kanban.html')


@main.route('/members')
@login_required
def members():
    if request.method == 'GET':
        return render_template('members.html')