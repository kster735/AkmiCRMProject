from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from minicrm.models import Agent, User, Contact, Message

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
        field_classes = {'username': UsernameField}

class ContactCreationForm(forms.ModelForm):    
    class Meta:
        model = Contact
        exclude = ('agent',)


