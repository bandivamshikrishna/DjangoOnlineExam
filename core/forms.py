from django import forms 
from django.contrib.auth.models import User



class SignUpForm(forms.ModelForm):
    role_category=[('Student','Student'),('Examiner','Examiner')]
    role=forms.CharField(max_length=100,widget=forms.Select(choices=role_category))
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}