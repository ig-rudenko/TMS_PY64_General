from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from notes.models import Note

User = get_user_model()  # Возвращает модель пользователя текущего проекта.


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        validate_password(password)
        return password

    def clean(self):
        """Валидация всей формы, автоматически вызывается."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            self.add_error("password2", "Пароли не совпадают")

        return cleaned_data


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
