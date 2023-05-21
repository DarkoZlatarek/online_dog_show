from .models import Comment, Enter
from django import forms


class EnterForm(forms.ModelForm):
    """
    Entry submission form
    """
    class Meta:
        model = Enter
        fields = (
            'title',
            'content',
            'featured_image',
        )


class CommentForm(forms.ModelForm):
    """
    Comment submission form
    """
    class Meta:
        model = Comment
        fields = ('body',)
