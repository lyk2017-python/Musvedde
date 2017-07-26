from django.conf.urls import url
from news.views import *

urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^category/(?P<pk>[A-Za-z0-9\-]+)$", CategoryView.as_view(), name="category_view"),
    url(r"^news/(?P<pk>\d+)$", NewsView.as_view(), name="news_view"),
]
