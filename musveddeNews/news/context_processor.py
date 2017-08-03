from news.models import Category


def category_processor(request):
    categories = Category.objects.filter()
    return {"categories": categories}
