from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=64)])
    email = EmailField("Email", validators=[DataRequired(), Length(min=6, max=255)])
    password = StringField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
