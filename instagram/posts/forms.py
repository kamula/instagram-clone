from django import forms
from .models import userPost

class createPostForm(forms.ModelForm):
    class Meta:
        model = userPost
        fields = ['image']
