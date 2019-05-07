from django import forms
from .models import login


class PollsForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['login_id', 'login_password']