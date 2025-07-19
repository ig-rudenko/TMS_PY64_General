from flask import Flask

from handlers.auth import auth_bp
from handlers.notes import notes_bp
from models import User
from settings import db, login_manager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "your-secret-key"

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

with app.app_context():
    db.create_all()


@login_manager.user_loader
def get_user_by_id(user_id: int) -> User | None:
    return User.query.get(user_id)


app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)
