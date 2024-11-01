from django.urls import path,include
from . import views
app_name='PatientApp'
urlpatterns = [
    path('', views.ProjectHomePage, name='ProjectHomePage'),
    path('PatientAppHomePage/', views.PatientHomePage, name='PatientHomePage'),
    path('logout/', views.logout, name='logout'),

]