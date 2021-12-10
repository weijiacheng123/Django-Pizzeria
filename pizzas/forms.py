from django import forms
from django.forms import fields, widgets
from .models import Comment, Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}
        #widgets = {'text': forms.Textarea(attrs={'cols':80})}

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('pizza', 'image')