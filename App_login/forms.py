from django.contrib.auth.forms import UserCreationForm
from django import forms
from App_login.models import *


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'employee_id', 'username', 'password1', 'password2',
                  'phone_number', 'profile_picture']
