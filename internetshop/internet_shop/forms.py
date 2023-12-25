from django import forms
from .models import Account, Enter_code, New_Password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Autorisation(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class Check_code(forms.ModelForm):
    class Meta:
        model = Enter_code
        fields = ['entered_code']

class New_password(forms.ModelForm):
    class Meta:
        model = New_Password
        fields = ['username', 'email', 'enter_new_password']