from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Account Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput() ,max_length=100)
    re_password = forms.CharField(label='Re-Password', widget=forms.PasswordInput() ,max_length=100)

def compare_re_password(self):
    if 'password' in self.cleaned_data:
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password == re_password and password:
            return re_password
    raise forms.ValidationError("Invalid Password")

def clean_username(self):
    username = self.cleaned_data['username']
    if not re.search(r'^\w+&', username):
        raise forms.ValidationError("Account name with special characters")
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return username
    raise forms.ValidationError("Account already exists")

def save(self):
    User.objects.create_user(username=self.cleaned_data['username'], email=self.cleanded_data['email'], password=self.cleanded_data['password'])