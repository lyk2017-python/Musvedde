from django.core.mail import send_mail
from django.views import generic
from .models import Post, Category, Tags, Comments
from django.http import Http404
from news.forms import CategorizeNewsForm, ContactForm, CommentForm


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
            post_data["categories"] = self.get_category().id
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_category()
        return context


class HomeView(generic.ListView):
    def get_queryset(self):
        return Post.objects.filter()


class NewsView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/post_detail.html"
    success_url = "."

    def get_post(self):
        post = Post.objects.filter(slug=self.kwargs["slug"], hidden=False)
        if post.exists():
            return post.get()
        else:
            raise Http404("Post not found")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            comment = kwargs["data"].copy()
            comment["post"] = self.get_post().id
            kwargs["data"] = comment
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_post()
        return context


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




