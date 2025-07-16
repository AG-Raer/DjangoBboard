from django import forms
from .models import Bb

class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price']
        labels = {
            'title': 'Заголовок',
            'content': 'Описание',
            'price': 'Цена',
        }