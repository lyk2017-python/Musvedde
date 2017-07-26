from django.conf.urls import url
from .views import *

urlPatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^category/(?P<slug>\w+)', CategoryView.as_view(), name="category_view"),
    url(r'^news/(?P<id>\d+)-(?P<slug>)', NewsView.as_view(), name="news_view")
]