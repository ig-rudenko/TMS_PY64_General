from django import forms

from posts.models import Post, Comment, User, Tag


class PostForm(forms.ModelForm):
    new_tags = forms.CharField(
        max_length=128, required=False, label="Новые теги", help_text="Введите через запятую"
    )

    class Meta:
        model = Post
        fields = ["title", "content", "image", "tags"]

    def clean_new_tags(self) -> list[str]:
        if self.cleaned_data["new_tags"]:
            new_tags = self.cleaned_data["new_tags"].split(",")
            return [tag.strip() for tag in new_tags]
        return []


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
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, label="Теги")
