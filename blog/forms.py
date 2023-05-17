from django import forms
from .models import Post

class Image(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'images'}