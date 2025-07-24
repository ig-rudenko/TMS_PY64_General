from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import PostForm, CommentForm
from .models import Post, Comment
from .services import create_post, update_post, create_comment, get_posts_list


def posts_list_view(request):
    # http://127.0.0.1:8000/posts/?search=python
    search: str = request.GET.get('search', '')  # python

    posts = get_posts_list(search=search)

    return render(request, 'posts/posts_list.html', {'posts': posts})


@login_required
def create_post_view(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = create_post(title=title, content=content, user=request.user, image=form.cleaned_data['image'])

            return redirect(reverse("post-view", args=(post.id,)))

    return render(request, 'posts/create.html', {"form": form})


def post_detail_view(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    context = {'post': post, "comment_form": CommentForm(), "comments_list": comments}
    return render(request, 'posts/detail.html', context)


@login_required
def edit_post_view(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    if post.owner != request.user:
        return HttpResponseForbidden("У вас нет прав на редактирование этой записи")

    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = update_post(post, title=title, content=content, image=form.cleaned_data['image'])

            return redirect(reverse("post-view", args=(post.id,)))

    return render(request, 'posts/edit.html', {"form": form})


@login_required
def add_comment_view(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = create_comment(post, user=request.user, content=form.cleaned_data['text'])

            # http://127.0.0.1:8000/posts/1/#comment-3
            # reverse("post-view", args=(post.id,))     -> /posts/1/
            # f"#comment-{comment.id}"                  -> #comment-3
            return redirect(reverse("post-view", args=(post.id,)) + f"#comment-{comment.id}")

    return render(request, 'posts/detail.html', {'post': post, "comment_form": form})