from django.core.mail import send_mail

from news.models import Category
from news.forms import ContactForm


def category_processor(request):
    categories = Category.objects.filter(sub_level=0)
    return {"categories": categories}


def contact_form(request):
    return {"contact_form": ContactForm}