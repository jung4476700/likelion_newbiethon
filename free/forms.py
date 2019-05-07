from django import forms
from .models import Free

class FreeForm(forms.ModelForm):
    class Meta:
        model = Free
        fields = ['author', 'title', 'body']