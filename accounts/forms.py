from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class LoginForm (forms.Form):
    username = forms.CharField(
    max_length=100,
    label='Kullanıcı Adı',
    widget=forms.TextInput(attrs={'class': 'form-control', 'data-placeholder': '  Seçiniz'})
    )

    password = forms.CharField(
    max_length=100,
    label='Parola',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-placeholder': '  Seçiniz'})
    )

    # kullanıcıyı doğrulama
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını yada parolayı yanlış girdiniz!')
        return super(LoginForm, self).clean()
