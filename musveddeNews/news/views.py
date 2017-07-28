from django.views import generic
from .models import Post, Category, Tags
from django.http import Http404
from news.forms import CategorizeNewsForm


# Create your views here.

class PostCreateView(generic.CreateView):
    model = Post
    success_url = "/"
    fields = [
        "title",
        "created_at",
        "featured_until",
        "image",
        "categories",
        "slug",
    ]


class CategoryView(generic.CreateView):
    form_class = CategorizeNewsForm
    template_name = "news/category_create.html"
    success_url = "."

    def get_category(self):
        query = Category.objects.filter(slug=self.kwargs["slug"])
        if query.exists():
            return query.get()
        else:
            raise Http404("Category not found")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["categories"] = [self.get_category()]
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_category()
        return context


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


class TagsView(generic.DetailView):
    model = Tags

