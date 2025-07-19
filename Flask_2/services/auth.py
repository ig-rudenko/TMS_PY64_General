from werkzeug.security import generate_password_hash, check_password_hash

from models import User
from settings import db


def create_user(username, email, password) -> bool:
    if User.query.filter_by(username=username).first():
        return False

    password_hash = generate_password_hash(password)
    user = User(username=username, email=email, password=password_hash)
    db.session.add(user)
    db.session.commit()
    return True


def check_user(username, password) -> User | None:
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
