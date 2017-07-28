from django import forms
from django.forms import HiddenInput
from news.models import Post


class CategorizeNewsForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id",
            "reported",
        ]
        widgets = {
            "categories": HiddenInput()
}