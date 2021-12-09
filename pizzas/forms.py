from django import forms
from django.forms import fields
from .models import Pizza, Topping, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}