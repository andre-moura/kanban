from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import secrets


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Registering blue prints
    from app.controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.models.tables import User, Project, UserProjects, Kanban, KanbanList, Task

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.shell_context_processor
    def make_shell_context():
        """Enabling the use of flask shell to test things out"""
        return dict(
            app=app,
            db=db,
            User=User
        )

    @app.cli.command("bootstrap")
    def bootstrap_data():
        """Populates the database with data"""
        db.session.add(User(name="Andre", email="andre@gmail.com", password="123456"))
        db.session.add(Project(name="Project X"))
        db.session.add(Project(name="Dragons"))
        db.session.add(UserProjects(id_user=1, id_project=1))
        db.session.add(UserProjects(id_user=1, id_project=2))
        db.session.add(Kanban(name='Sprint 1', id_project=1))
        db.session.add(Kanban(name='Sprint 2', id_project=1))
        db.session.add(KanbanList(name='To do', order=1, id_kanban=1))
        db.session.add(KanbanList(name='Doing', order=2, id_kanban=1))
        db.session.add(KanbanList(name='Testing', order=3, id_kanban=1))
        db.session.add(KanbanList(name='Done', order=4, id_kanban=1))
        db.session.add(Task(content="Create a login page and connect with back-end", id_list=1))
        db.session.add(Task(content="Integrate the back-end and the front-end", id_list=1))
        db.session.add(Task(content="Create a task in the kanban", id_list=2))
        db.session.add(Task(content="Create the login route", id_list=2))
        db.session.add(Task(content="Create a register route", id_list=3))
        db.session.add(Task(content="Prototype the landing page", id_list=3))

        db.session.commit()

    return app