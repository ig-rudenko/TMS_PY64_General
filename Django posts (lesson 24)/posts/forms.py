from django import forms

from posts.models import Post, Comment, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

        widgets = {"text": forms.Textarea(attrs={"rows": 4})}


class PostSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск")
    user = forms.CharField(max_length=100, required=False, label="Пользователь")

    # Для Crispy Forms
    # user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Пользователь")
