from django import forms
from .models import post


class InputPosts(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'detail')
