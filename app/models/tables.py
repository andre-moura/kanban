from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password, method='sha256')

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def __repr__(self) -> str:
        user = {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
        return str(user)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        project = {
            'id': self.id,
            'name': self.name
        }
        return str(project)
    

class UserProjects(db.Model):
    __tablename__ = 'user_projects'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_project = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, id_user, id_project):
        self.id_user = id_user
        self.id_project = id_project

    def __repr__(self) -> str:
        user_projects = {
            'id': self.id,
            'id_user': self.id_user,
            'id_project': self.id_project
        }
        return str(user_projects)


class Kanban(db.Model):
    __tablename__ = 'kanbans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_project = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, name, id_project):
        self.name = name
        self.id_project = id_project

    def __repr__(self) -> str:
        kanban = {
            'id': self.id,
            'name': self.name,
            'id_project': self.id_project
        }
        return str(kanban)


class KanbanList(db.Model):
    __tablename__ = 'kanban_lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    order = db.Column(db.Integer)
    id_kanban = db.Column(db.Integer, db.ForeignKey('kanbans.id'))
    
    def __init__(self, name, order, id_kanban):
        self.name = name
        self.order = order
        self.id_kanban = id_kanban

    def __repr__(self) -> str:
        kanban_list = {
            'id': self.id,
            'name': self.name,
            'order': self.order,
            'id_kanban': self.id_kanban
        }
        return str(kanban_list)


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id_list = db.Column(db.Integer, db.ForeignKey('lists.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __init__(self, content, id_list):
        self.content = content
        self.id_list = id_list

    def __repr__(self) -> str:
        task = {
            'id': self.id,
            'content': self.content,
            'id_list': self.id_list,
            'id_user': self.id_user
        }
        return f'<Task {self.content}>'