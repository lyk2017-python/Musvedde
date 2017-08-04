from django.contrib import admin
from news.models import Category, Post, Tags, Comments

# Register your models here.


class PostChildrenInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryChildrenInline(admin.StackedInline):
    model = Category
    extra = 0
    fk_name = "parent"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "parent",
        "slug",
    ]

    search_fields = [
        "name",
        "slug",
    ]

    inlines = [PostChildrenInline, CategoryChildrenInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "reported"
    ]
    search_fields = [
        "title",
        "slug",
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "featured_until",
        "reported",
        "liked",

    ]

    fieldsets = [
        (
            "Global",
            {
                "fields": [
                  ("title", "slug"),
                  "content",
                  ("liked", "reported", "read"),
                  "source",
                  "image",
                  ("categories", "tags"),
                ]
            }
        ),
        (
            "Dates",
            {
                "fields": [
                    ("created_at", "featured_until")
                ]
            }
        )
    ]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = [
        "tag",
        "slug",
    ]

    search_fields = [
        "tag",
        "slug",
    ]


@admin.register(Comments)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "comment",
        "post",
        "created_at",
        "hidden",
        "reported",
        "user_email",
    ]

    search_fields = [
        "comment",
        "post",
        "user_name",
        "user_email"
    ]

    list_filter = [
        "created_at",
        "reported",
        "liked_count",

    ]

