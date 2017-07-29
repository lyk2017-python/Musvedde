from django.core.mail import send_mail
from django.views import generic
from .models import Post, Category, Tags
from django.http import Http404
from news.forms import CategorizeNewsForm,ContactForm


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
    template_name = "news/category_detail.html"
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


class NewsView(generic.DetailView):
    model = Post


class TagsView(generic.DetailView):
    model = Tags


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "news/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
            "Musvedde ContactForm : {}".format(data["subject"]),
            ("You have a notification\n"
             "---\n"
             "{}\n"
             "---\n"
             "email={}\n"
             "ip={}").format(data["message"], data["email"], self.request.META["REMOTE_ADDR"]),
            settings.DEFAULT_FROM_EMAIL,
            ["hamuha@musvedde.com"]
        )
        return super().form_valid(form)



