from django.core.mail import send_mail
from django.views import generic
from .models import Post, Category, Tags, Comments, UserLikes, Reports
from django.http import Http404, JsonResponse
from django.db.models import F
from news.forms import CategorizeNewsForm, ContactForm, CommentForm, NewsForm, CustomUserCreationForm, ReportForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CategoryView(generic.CreateView):
    form_class = CategorizeNewsForm
    template_name = "news/category_detail.html"
    success_url = "."

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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

class SearchView(generic.ListView):
    model = Post


class HomeView(generic.CreateView):
    form_class = NewsForm
    template_name = "news/post_list.html"
    success_url = "."

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(hidden=False)
        context["most_viewed"] = context["posts"].order_by("-read")[:5]
        context["most_liked"] = context["posts"].order_by("-liked")[:5]
        return context


class NewsSearchingView(SearchView):
    template_name = "news/search.html"


    def get_queryset(self):
        result = super(SearchView, self).get_queryset()

        query = self.request.GET.get("q")
        if query:
            result = result.filter(title__icontains=query)

        return result


class NewsView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/post_detail.html"
    success_url = "."

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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
            comment["user"] = self.request.user.id
            kwargs["data"] = comment
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_post()
        if self.request.method == "GET":
            context["post"].read += 1
            context["post"].save()
            context["liked"] = None
            context["report_form"] = ReportForm
            if self.request.user.is_authenticated():
                if UserLikes.objects.filter(post=self.get_post(), user=self.request.user):
                    context["liked"] = True
                else:
                    context["liked"] = False
        return context


def likeButton(request):
    if request.method == "POST":
        id= request.POST.get("id", default=None)
        post = get_object_or_404(Post, id=int(id))
        like = UserLikes.objects.filter(user=request.user, post=post)
        if not like:
            UserLikes.objects.create(user=request.user, post=post)
            post.liked = F("liked") + 1
            post.save(update_fields=["liked"])
            status = "added"
        else:
            like.delete()
            post.liked = F("liked") - 1
            post.save(update_fields=["liked"])
            status = "deleted"
        post.refresh_from_db()
    return JsonResponse({"status": status, "likes": post.liked})


class TagsView(generic.DetailView):
    model = Tags


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "news/base.html"
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
            ["gshakan16@gmail.com"]
        )
        return super().form_valid(form)



class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "news/login.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
