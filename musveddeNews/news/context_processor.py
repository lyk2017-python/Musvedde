from news.models import Category


def category_processor(request):
    categories = Category.objects.filter(sub_level=0)
    return {"categories": categories}
