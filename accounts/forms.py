from django.contrib.auth.forms import UserCreationForm 
from django.db import models
from django.contrib.auth.models import User

#create forms
class customUserCreationForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields =  ('username','email', 'password1', 'password2' )