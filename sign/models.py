from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

# Таблица для сверки пользователя с паролем
class OneTimeCode(models.Model):
    user = models.CharField(max_length=255)
    code = models.CharField(max_length=10)


class BaseRegisterForm(UserCreationForm):
    username = forms.CharField(label="Псевдоним")

    email = forms.EmailField(label="Email")


    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2", )

