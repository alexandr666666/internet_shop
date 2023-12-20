from django import forms
from .models import Account, Enter_code, Card_Number
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

class Card_number(forms.ModelForm):
    class Meta:
        model = Card_Number
        fields = ['card_number']