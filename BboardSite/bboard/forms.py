from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bb

class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'image']
        labels = {
            'title': 'Заголовок',
            'content': 'Описание',
            'price': 'Цена',
            'image': 'Изображение',
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Введите действительный email.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже зарегистрирован.')
        return email