import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Post(models.Model):
    """ Class for Post News """
    title = models.CharField(max_length=160)
    content = models.TextField()
    source = models.URLField(null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True, default=None)
    liked = models.IntegerField(default=0)
    reported = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tags")
    slug = models.SlugField(max_length=160, blank=True, unique=True)
    hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    featured_until = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Category(models.Model):
    """ Class for Categories """
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey("self", blank=True, null=True, default=None)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    sub_level = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tags(models.Model):
    """ Class for Tags """
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return "{}".format(self.tag)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Comments(models.Model):
    """ Class for Comments """
    comment = models.TextField()
    post = models.ForeignKey("Post")
    liked_count = models.PositiveIntegerField(default=0)
    reported_count = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateField(default=datetime.datetime.now)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()

    def __str__(self):
        return "{} - {}".format(self.comment,self.user_email)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


@receiver(pre_save, sender=Post)
@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Tags)
def define_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        elif hasattr(sender, "title"):
            instance.slug = slugify(instance.title)
        elif hasattr(sender, "tag"):
            instance.slug = slugify(instance.tag)
        else:
            raise AttributeError("It needs name, tag or title to define slug")
    return instance


@receiver(pre_save, sender=Post)
def auto_hidden(sender, instance, *args, **kwargs):
    if instance.reported >= 10:
        instance.hidden = True
    return instance


