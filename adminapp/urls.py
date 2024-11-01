from django.urls import path, include
from .import views
from django.urls import path

from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns=[
    path('', views.ProjectHomePage, name='ProjectHomePage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatepagecall/', views.calculatepagecall, name='calculatepagecall'),
    path('calculatelogic/', views.calculatelogic, name='calculatelogic'),
    path('add_task/',views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    #path('add_student/', views.add_student, name='add_student'),
    #path('facultyapp/',include('facultyapp.urls',namespace='facultyapp')),
    #path('studentapp/',include('studentapp.urls',namespace='studentapp')),
    path('AddStudent/', views.add_student, name='AddStudent'),
    path('student list/', views.student_list, name='student list'),
    path('upload_file/', views.upload_file, name='upload_file'),
    # path('add_course/', views.add_course, name='add_course'),
    # path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('contact_manager/',views.contact_manager, name='contact_manager'),


]