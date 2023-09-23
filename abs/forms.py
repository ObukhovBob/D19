from django import forms
from .models import Ads, Post
from django_ckeditor_5.widgets import CKEditor5Widget


class AdsCreateForm(forms.ModelForm):

    class Meta:
        model = Ads
        fields = ('header', 'position', 'text_ads')
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="default"
            )
        }
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        self.fields['text_ads'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['text_ads'].required = False

class AdsUpdateForm(AdsCreateForm):

    class Meta:
        model = Ads
        fields = AdsCreateForm.Meta.fields

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['text_ads'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['text_ads'].required = False

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text_post',)


class PostUpdateForm(PostCreateForm):

    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields
