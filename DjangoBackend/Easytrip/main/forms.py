from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField( widget=forms.PasswordInput)
    password2 = forms.CharField( widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'email': TextInput(attrs={'placeholder': 'Адрес электронной почты'}),
            'country': TextInput(attrs={'placeholder': 'Страна проживания'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match.')
        return cd['password2']

