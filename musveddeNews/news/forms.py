from django import forms
from django.forms import HiddenInput
from news.models import Post


class CategorizeNewsForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id",
            "reported",
            "created_at",
            "featured_until",
            "liked",
            "hidden"
        ]
        widgets = {
            "categories": HiddenInput()
        }


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=160)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))