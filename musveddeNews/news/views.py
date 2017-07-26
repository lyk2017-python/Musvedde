from django.views import generic
from .models import Post, Category
from datetime import datetime, timedelta

# Create your views here.


class HomeView(generic.ListView):
    def get_queryset(self):
        return Post.objects.filter()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryView(generic.DetailView):
    model = Category


class NewsView(generic.DetailView):
    model = Post

