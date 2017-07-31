from django import forms
from django.forms import HiddenInput
from news.models import Post, Tags, Comments


class NewsForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), required=False)
    tag_names = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(NewsForm, self).clean()
        tags = set(cleaned_data.get("tags"))
        tag_names = cleaned_data.get("tag_names")
        tag_names_list = tag_names.split(",")
        for t in tag_names_list:
            if t:
                obj, is_created = Tags.objects.get_or_create(tag=t)
                tags.add(obj)
        if not tags:
            raise forms.ValidationError(
                "En az bir tag seçmeli ya da yazmalısınız"
            )
        cleaned_data["tags"] = tags
        return cleaned_data
    
    class Meta:
        model = Post
        exclude = [
            "id",
            "reported",
            "created_at",
            "featured_until",
            "liked",
            "hidden",
            "slug",
        ]


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=160)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments

        exclude = [
            "id",
            "created_at",
            "reported",
            "hidden",
            "liked_count",
        ]
        widgets = {
            "post": HiddenInput()
        }


class CategorizeNewsForm(NewsForm):
    class Meta:
        model = Post
        exclude = [
            "id",
            "reported",
            "created_at",
            "featured_until",
            "liked",
            "hidden",
            "slug",
        ]
        widgets = {
            "categories": HiddenInput()
        }