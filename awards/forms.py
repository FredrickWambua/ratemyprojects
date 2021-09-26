from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, Project, Rates
from django import forms
from django.db import models
from django.forms import fields, widgets



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'location', 'bio']

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image','description', 'link']

class RatesUploadForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['design', 'content', 'usability']
