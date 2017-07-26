from django.shortcuts import render
from django.views import generic
from .models import Post, Category
from datetime import datetime, timedelta

# Create your views here.


class HomeView(generic.ListView):
    def get_queryset(self):
        one_week_ago = datetime.today() - timedelta(days=7)
        return Post.objects.filter(created_at__gte=one_week_ago)


class CategoryView(generic.DetailView):
    def get_queryset(self, pk):
        category = Category.objects.get(id=pk)
        return Post.objects.filter(categories=category)


class NewsView(generic.DetailView):
    def get_queryset(self):
        return Post.objects.filter()
