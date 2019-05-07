from django import forms
from .models import Apply

class PostForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['title', 'author', 'body']