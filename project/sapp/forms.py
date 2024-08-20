from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Post
        fields = ['post_autor',
                  'post_catagory',
                  'articles_or_news',
                  'datetime',
                  'title',
                  'text',
                  # 'rating_pos',
                  'added_at']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту."
            )

        return cleaned_data