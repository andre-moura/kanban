from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '65a19a98-e2d1-4bfa-98bf-a8feec4ec0ed'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models.tables import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=db,
            User=User
        )

    from app.controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


# from app.controllers import auth
# from app.controllers import main

