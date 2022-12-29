from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user
from app.models.tables import UserProjects, Project, Kanban, KanbanList, Task
from app import db
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/projects', methods=['GET', 'POST'])
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
        project_name = request.form['project-name']
        new_project = Project(
            name=project_name
        )
        new_user_project = UserProjects(
            id_user=current_user.id, 
            id_project=new_project.id
        )

        db.session.add(new_project)
        db.session.add(new_user_project)
        db.session.commit()
        return redirect(url_for('main.projects'))

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
        return render_template('boards.html', kanbans=kanbans, id_project=id)
    

@main.route('/boards', methods=['POST'])
@login_required
def create_board():
    if request.method == 'POST':
        id_project = request.form['board_submit']
        board_name = request.form['board_name']

        board = Kanban(
            name=board_name, 
            id_project=id_project
        )

        db.session.add(board)
        db.session.commit()
        return redirect(url_for('main.boards', id=id_project))


@main.route('/list', methods=['POST'])
@login_required
def list():
    if request.method == 'POST':
        id_kanban = request.form['kanban_submit']
        list_name = request.form['list_name']
        order = db.session.query(func.max(KanbanList.order)).filter_by(id_kanban=id_kanban).one()[0]

        if not order:
            order = 1
        else:
            int(order)
            order += 1
            
        new_kanban_list = KanbanList(
            name=list_name,
            id_kanban=id_kanban,
            order=order
        )
        db.session.add(new_kanban_list)
        db.session.commit()
        return redirect(url_for('main.kanban', id=id_kanban))

@main.route('/kanban/<id>', methods=['GET', 'POST'])
@login_required
def kanban(id):
    if request.method == 'GET':
        kanban_lists = KanbanList.query.filter_by(id_kanban=id).order_by(KanbanList.order).all()
        ids_lists = []
        for kanban_list in kanban_lists:
            ids_lists.append(kanban_list.id)
        tasks = Task.query.filter(Task.id_list.in_(tuple(ids_lists))).all()
        return render_template('kanban.html', kanban_lists=kanban_lists, tasks=tasks, id_kanban=id)


@main.route('/members')
@login_required
def members():
    if request.method == 'GET':
        return render_template('members.html')