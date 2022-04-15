from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Create your models here.

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username',)