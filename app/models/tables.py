from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email


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
