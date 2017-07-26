from django.conf.urls import url
from news.views
urlspatterns =[url(r"^$",homepage_show.as_view()),
               url(r"^kategori/(?P<slug>[A-Za-z0-9\-]+)$",category_show.as_view())
               url(r"^detay/(_P<id>\d-(?P<slug>[A-Za-z0-9\-]+)$",detail_show.as_view() )]