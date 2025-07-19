from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=512)])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Create")
