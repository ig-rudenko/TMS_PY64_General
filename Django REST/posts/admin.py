from django.contrib import admin
from django.db import models
from django.db.models.functions import Upper, Lower
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ("text", "owner", "created_at")
    readonly_fields = ("created_at",)
    extra = 1


class TagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_at",
        "updated_at",
        "image_preview",
        "comments_count",
        "tags_list",
    )
    search_fields = ("title", "content")
    list_filter = ("owner",)
    date_hierarchy = "created_at"
    fieldsets = (
        (
            None,
            {"fields": ("title", "image_preview", "content", "owner", "image")},
        ),
    )
    readonly_fields = ("image_preview",)
    inlines = [CommentInline, TagInline]
    actions = ["to_lower_case", "to_upper_case"]

    @admin.display(description="Превью изображения")
    def image_preview(self, obj: Post):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='100px' />")
        return "-"

    @admin.display(description="Кол-во комментариев")
    def comments_count(self, obj: Post):
        if hasattr(obj, "comments_count"):
            return obj.comments_count

        # return Comment.objects.filter(post=obj).count()
        # Либо так:
        return obj.comment_set.count()

    @admin.display(description="Теги")
    def tags_list(self, obj: Post):
        text = ""

        # Tag.objects.filter(post=obj)
        # Это тоже самое:
        for tag in obj.tags.all():
            text += f"<li>{tag.name}</li>"

        return mark_safe(text)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # prefetch_related только для many-to-many
        qs = qs.annotate(comments_count=models.Count("comment")).prefetch_related("tags")
        return qs

    @admin.action(description="В нижний регистр")
    def to_lower_case(self, request, queryset):
        # UPDATE "posts" SET "title" = LOWER("posts"."title") WHERE
        qs = queryset.update(title=Lower(models.F("title")))

    @admin.action(description="В верхний регистр")
    def to_upper_case(self, request, queryset):
        # UPDATE "posts" SET "title" = UPPER("posts"."title") WHERE
        qs = queryset.update(title=Upper(models.F("title")))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "posts_count")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(posts_count=models.Count("post"))
        return qs

    @admin.display(description="Кол-во постов")
    def posts_count(self, obj: Tag):
        if hasattr(obj, "posts_count"):
            return obj.posts_count

        # return Posts.objects.filter(tags=obj).count()
        # Либо так:
        return obj.post_set.all().count()
