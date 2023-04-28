from .models import Comment, Enter
from django import forms


class EnterForm(forms.ModelForm):
    class Meta:
        model = Enter
        fields = (
            'title',
            'content',
            'featured_image',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
