from django import forms
from django.contrib.auth.models import User
from .models import contactus, userProfile, blog


class contactusForm(forms.ModelForm):
    class Meta:
        model   = contactus
        fields  = ["fullname", "phone_num", "email", "message"]
        widgets = {
            'fullname': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.NumberInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'})
        }



class userProfileForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'})
        }



class userProfileUpdateForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num', 'profile_pic']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'style' : 'margin-top:15px'}),
        }



class userUpdateForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'})
        }



class blogForm(forms.ModelForm):
    class Meta:
        model   = blog
        fields  = ['category', 'title', 'description', 'image']
        widgets = {
            'category': forms.TextInput(attrs={'class' : 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={'class' : 'form-control'}),
            'image': forms.FileInput(attrs={'style' : 'margin-top:15px'})
        }


class blogEditForm(forms.ModelForm):
    class Meta:
        model   = blog
        fields  = ['category', 'title', 'description', 'image']
        widgets = {
            'category': forms.TextInput(attrs={'class' : 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={'class' : 'form-control'}),
            'image': forms.FileInput(attrs={'style' : 'margin-top:15px'})
        }