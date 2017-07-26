import datetime
from django.db import models


class Post(models.Model):
    """ Class for Post News """
    title = models.CharField(max_length=160)
    content = models.TextField()
    slug=models.SlugField()
    image = models.ImageField(null=True, blank=True, default=None)
    liked = models.IntegerField(default=0)
    reported = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tags")
    slug = models.SlugField(max_length=160)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    featured_until = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Category(models.Model):
    """ Class for Categories """
    name = models.CharField(max_length=50,unique=True)
    parent = models.ForeignKey("self", default=0)

    def __str__(self):
        return "{}".format(self.name)


class Tags(models.Model):
    """ Class for Tags """
    tag = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.tag)
