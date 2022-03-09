"""DjangoOnlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',views.home,name='home'),
    path('signin/',views.sign_in,name='signin'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/afterlogin/',views.after_login,name='afterlogin'),
    path('admindashboard/',views.admin_dashboard,name='admindashboard'),
    path('logout',views.account_logout,name='logout'),
    path('student/',views.student_form,name='student'),
    path('admineb/',views.admin_examination_branch,name='admineb'),
    path('admineb/subject/',views.admineb_subject,name='adminebsubject'),
    path('admineb/subject/new',views.admineb_subject_new,name='adminebsubjectnew'),
    path('admineb/subject/edit',views.admineb_subject_edit,name='adminebsubjectedit'),
    path('admineb/topic/',views.admineb_topic,name='adminebtopic'),
    path('admineb/topic/new',views.admineb_new_topic,name='adminebtopicnew'),
    path('admineb/topic/edit',views.admineb_edit_topic,name='adminebtopicedit'),
    path('admineb/question/',views.admineb_question,name='adminebquestion'),
    path('admineb/question/new/',views.admineb_new_question,name='adminebquestionnew'),
    path('admineb/question/edit/',views.admineb_edit_question,name='adminebquestionedit'),

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)