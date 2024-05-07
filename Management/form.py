from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import User
from .models import Menu
from django.forms import ModelForm

class signUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password','groups']

class AddNewMenuItem(ModelForm):
    class Meta:
        model=Menu
        fields='__all__'