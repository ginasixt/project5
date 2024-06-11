from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Group, Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'location' ,  'description',  'activity']

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    