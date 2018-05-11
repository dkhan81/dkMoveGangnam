from django import forms

from .models import Post, Resume

class PostForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('title', 'text', 'tech', 'emp_period')