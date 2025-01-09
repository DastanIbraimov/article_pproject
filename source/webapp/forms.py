from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)  # по умолчанию required=True
    author = forms.CharField(label='Author', max_length=50, required=False, initial='Anonymous',
                             widget=widgets.TextInput(attrs={'placeholder': 'Author'}))
    content = forms.CharField(label='Content',
                              widget=forms.Textarea(attrs={'cols': 25, 'rows': 5, 'placeholder': 'Enter your article'}),
                              required=False)
