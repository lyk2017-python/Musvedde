from django.contrib import admin
from news.models import Category,Post,Tags

# Register your models here.


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
                  ("liked", "reported"),
                  "image",
                  "categories",
                ]
            }
        ),
        (
            "Dates",
            {
                "fields": [
                    ("created_at", "featured_for")
                ]
            }
        )
    ]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

