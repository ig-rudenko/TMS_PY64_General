from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_user, logout_user

from forms.auth import RegisterForm, LoginForm
from services.auth import create_user, check_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if create_user(username=form.username.data, email=form.email.data, password=form.password.data):
            return redirect(url_for("auth.login"))

        if not form.username.errors:
            form.username.errors = []
        form.username.errors.append("Username already exists")

    return render_template("login/signup.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = check_user(username=form.username.data, password=form.password.data)
        if user:
            # Входим. Создается cookie нашей сессии
            login_user(user)
            return redirect(url_for("notes.notes"))

    return render_template("login/login.html", form=form)


@auth_bp.post("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
