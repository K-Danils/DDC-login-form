from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets

from .routes import URL_INDEX

# init SQLAlchemy
db = SQLAlchemy()

def create_app():
    # initializes the app, login manager etc.

    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex() # ATTENTION !!! will need security rework if deployed for major audience
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = URL_INDEX
    login_manager.init_app(app)

    from .user_model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
    