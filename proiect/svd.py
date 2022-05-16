from django import forms
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password
from django.contrib.auth import get_user_model
from .get_page import Profile as PROFILE
from .get_page import Repo as REPO
from .get_page import get_page as get_page
from .models import Profile, Repo
from django.db import models


class RegisterProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'fullname', 'username',
                  'bio', 'followers', 'following']

    image = forms.CharField(max_length=60)
    fullname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=200)
    followers = forms.CharField(max_length=50)
    following = forms.CharField(max_length=50)

    def __init__(self, image, fullname, username, bio, followers, following):
        self.image = image
        self.fullname = fullname
        self.username = username
        self.bio = bio
        self.followers = followers
        self.following = following

    def save(self, commit=True):
        return super().save(commit)
