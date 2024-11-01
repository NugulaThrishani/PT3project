from django.urls import path, include
from .import views
from django.urls import path
urlpatterns=[
    path('', views.ProjectHomePage, name='ProjectHomePage'),


    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserSignUpPageCall/', views.UserSignUpPageCall, name='UserSignUpPageCall'),
    path('UserSignUpLogic/', views.UserSignUpLogic, name='UserSignUpLogic'),
    path('SignUpSuccessful/', views.SignUpSuccessful, name='SignUpSuccessful'),
    path('about/', views.about, name='about'),
   #path('LoginHomePage/', views.LoginHomePage, name='LoginHomePage'),
    path('DoctorHomePage/', views.DoctorHomePage, name='DoctorHomePage'),
    path('PatientHomePage/', views.PatientHomePage, name='PatientHomePage'),





    #path('PatientApp/',include('PatientApp.urls',namespace='PatientApp')),
    #path('AdminApp/',include('AdminApp.urls',namespace='AdminApp')),

]