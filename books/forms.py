from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from books.models import Plik, Katalog


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Plik
        fields = ('nazwa', 'adres')


class NewDirectory(forms.ModelForm):
    class Meta:
        model = Katalog
        fields = ('nazwa',)

