from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'core/home.html')


def sign_in(request):
    authform=AuthenticationForm()
    return render(request,'core/signin.html',{'authform':authform})