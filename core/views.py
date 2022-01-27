from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')


def sign_in(request):
    return render(request,'core/signin.html')