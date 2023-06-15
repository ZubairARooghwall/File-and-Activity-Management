from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

#Import all the models
from .models import User

class MyUserRegistrationFrom(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'bio', 'avatar', 'prefers_dark_theme']


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'username', 'email', 'bio', 'avatar']
		
		# in form, you add enctype="multipart/form-data"
		# in views.py, form = UserForm(..add request.FILES...)