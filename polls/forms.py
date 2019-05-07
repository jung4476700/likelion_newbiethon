from django import forms
from .models import Polls


class PollsForm(forms.ModelForm):
    class Meta:
        model = Polls
        fields = ['title', 'author', 'video_key', 'body']
        
        
