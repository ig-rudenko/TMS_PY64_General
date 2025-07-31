from django.contrib import admin
from django.db import models
from django.db.models.functions import Upper, Lower
from django.utils.safestring import mark_safe

from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ("text", "owner", "created_at")
    readonly_fields = ("created_at",)
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at", "image_preview", "comments_count")
    search_fields = ("title", "content")
    list_filter = ("owner",)
    date_hierarchy = "created_at"
    fieldsets = ((None, {"fields": ("title", "image_preview", "content", "owner", "image")}),)
    readonly_fields = ("image_preview",)
    inlines = [CommentInline]
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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(comments_count=models.Count("comment"))
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
