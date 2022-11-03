
from django import forms
from django.contrib.auth.models import User
from .models import *

class reg_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']

class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location','job_title','pic']

class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','content']

# Create your models here.
