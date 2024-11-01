from django.urls import path, include
from . import views
app_name='AdminApp'

urlpatterns = [
       path('', views.ProjectHomePage, name='ProjectHomePage'),
       path('DoctorHomePage/', views.DoctorHomePage, name='DoctorHomePage'),
       path('logout/', views.logout, name='logout'),
]