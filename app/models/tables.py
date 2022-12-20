from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass
    

class ProjectUser:
    __tablename__ = 'projects_users'

    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_project = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, id_user, id_project):
        self.id_user = id_user
        self.id_project = id_project

    def __repr__(self):
        pass


class Kanban(db.Model):
    __tablename__ = 'kanbans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_project = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, name, id_project):
        self.name = name
        self.id_project = id_project

    def __repr__(self):
        pass


class KanbanList(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    order = db.Column(db.Integer)
    id_kanban = db.Column(db.Integer, db.ForeignKey('kanbans.id'))
    
    def __init__(self, name, order, id_kanban):
        self.name = name
        self.order = order
        self.id_kanban = id_kanban

    def __repr__(self):
        pass


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        pass