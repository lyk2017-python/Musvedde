import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, default=None)
    liked = models.IntegerField(default=0)
    reported = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tags")
    slug = models.SlugField(max_length=160)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    featured_until = models.DateTimeField(default=None, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", default=0)


class Tags(models.Model):
    tag = models.CharField(max_length=50)
