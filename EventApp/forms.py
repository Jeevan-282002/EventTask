from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from . models import Event


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Your Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User




class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
          
            "username":"Enter Your username",
            "email": "Enter Your Email",
            "password1": "Enter Your password",
            "password2": "Confirm your password",


        }
        widgets = {
     
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'date', 'time', 'location',"image")

        labels = {
          
            "event_name":"Enter Event name",
            "date": "Enter Event date",
            "time": "Enter Event time",
            "location": "Enter Event location",
            "image": "Enter Event image",


        }
        widgets = {
     
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'time': forms.TimeInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            
            
        }