from news.models import Category


def category_processor(request):
    return {"categories": Category.objects.filter(sub_level=0)}
