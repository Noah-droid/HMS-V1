from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib import messages


class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        demail = self.cleaned_data['email']
        if "lcu.edu" not in demail:
            raise forms.ValidationError("You must use the school Email ID. Try using this: yourusername@students.lcu.edu")
            message = "You already Booked the Room One can Book Only one Room"
            messages.error(request, message)
            return redirect('register_page')
        return demail

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','guardian_name','guardian_num','Gender','Dept','level', 'email','matric','phone_number','password1', 'password2']


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ['guardian_name','guardian_num','Gender','Dept','level', 'email','matric','phone_number']


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("username", 'last_name')
            