from django import forms
from .models import books


class bookform(forms.ModelForm):
    class Meta:
        model = books
        fields = ['name', 'desc', 'year', 'img']
