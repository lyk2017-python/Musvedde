from news.forms import ContactForm
from news.models import Category


def category_processor(request):
    categories = Category.objects.filter()
    return {"categories": categories}


def contact_form(request):
    contactform = ContactForm()
    return {"contact_form": contactform}
