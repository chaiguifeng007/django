from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    passowrd = forms.CharField(widget=forms.PasswordInput)
    # passowrd_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'passowrd']