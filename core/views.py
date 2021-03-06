from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.models import Group,User
from student import models as stu_models 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from student.forms import StudentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'core/home.html')

def sign_up(request):
    if request.method=='POST':
        signupform=SignUpForm(request.POST)
        student=stu_models.StudentForm()
        if signupform.is_valid():
            role=signupform.cleaned_data.get('role')
            if role=='Student':
                user=signupform.save()
                student.user=user
                student.save()
                student_group,created=Group.objects.get_or_create(name=role)
                user.groups.add(student_group)
                return HttpResponseRedirect('/signin/')
    else:
        signupform=SignUpForm()
    return render(request,'core/signup.html',{'signupform':signupform})



def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            authform=AuthenticationForm(request=request,data=request.POST)
            if authform.is_valid():
                username=authform.cleaned_data.get('username')
                password=authform.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('afterlogin')
        else:
            authform=AuthenticationForm()
            return render(request,'core/signin.html',{'authform':authform})
    else:
        return HttpResponseRedirect('afterlogin')
        



def after_login(request):
    user=request.user
    if user.groups.filter(name='Students'):
        return HttpResponseRedirect('/student/dashboard/')
    if user.is_superuser:
        return HttpResponseRedirect('/admindashboard/')
    else:

        return HttpResponseRedirect('/student/')
    


def student_form(request):
    user=request.user
    data=User.objects.get(first_name=user.first_name)
    student=StudentForm(instance=data)
    student2=SignUpForm(instance=data)
    return render(request,'student/studentforms.html',{'student':student,'student2':student2})


def account_logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')


@login_required
def admin_dashboard(request):
    return render(request,'core/admindashboard.html')


@login_required
def admin_examination_branch(request):
    return render(request,'core/examinationbranch.html')


@login_required
def admineb_subject(request):
    return render(request,'core/definesubject.html')


@login_required
def admineb_subject_new(request):
    return render(request,'core/definenewsubject.html')

@login_required
def admineb_subject_edit(request):
    return render(request,'core/defineeditsubject.html')


@login_required
def admineb_topic(request):
    return render(request,'core/definetopic.html')


@login_required
def admineb_new_topic(request):
    return render(request,'core/definenewtopic.html')


@login_required
def admineb_edit_topic(request):
    return render(request,'core/defineedittopic.html')

@login_required
def admineb_question(request):
    return render(request,'core/definequestion.html')

@login_required
def admineb_new_question(request):
    return render(request,'core/definenewquestion.html')

@login_required
def admineb_edit_question(request):
    return render(request,'core/defineeditquestion.html')