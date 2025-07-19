from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import current_user, login_required

from forms.notes import NoteForm
from models import Note
from services.notes import create_note

notes_bp = Blueprint("notes", __name__, url_prefix="/notes")


@notes_bp.get("/")
def notes():
    print(current_user)
    print(current_user.username)
    return render_template("notes/main.html", notes=[])


@notes_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_note_view():
    form = NoteForm()

    if form.validate_on_submit():
        note = create_note(current_user.id, form.title.data, form.content.data)
        return redirect(url_for("notes.view_note", note_id=note.id))

    return render_template("notes/create.html", form=form)


@notes_bp.get("/<int:note_id>")
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        abort(403)
    return render_template("notes/view.html", note=note)


@notes_bp.route("/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    pass


@notes_bp.post("/<int:note_id>/delete")
@login_required
def delete_note(note_id):
    pass
