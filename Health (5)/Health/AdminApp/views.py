from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import pytz

#create your views
from django.shortcuts import render
from django.shortcuts import render, redirect

from.forms import TaskForm
from .models import Task



def ProjectHomePage(request):
    return render(request,'AdminApp/ProjectHomePage.html')

def about(request):
    return render(request,'AdminApp/About.html')
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('add_task')

def register(request):
    return render(request, 'AdminApp/UserSignUpPage.html')


def login(request):
    return render(request, 'AdminApp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')

from datetime import datetime, timedelta
from django.shortcuts import render



from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.http import HttpResponseRedirect



def UserSignUpPageCall(request):
    return render(request, 'AdminApp/UserSignUpPage.html')
def UserSignUpLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username)
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'AdminApp/UserSignUpPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'AdminApp/UserSignUpPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'AdminApp/SignUpSuccessful.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'AdminApp/UserSignUpPage.html')
    else:
        return render(request, 'SignUpSuccessful.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def UserLoginPageCall(request):
    return render(request, 'AdminApp/UserLoginPage.html')
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('PatientHomePage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as PatientApp!')
                return redirect('DoctorHomePage')  # Replace with your PatientApp homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or PatientApp criteria.')
                return render(request, 'AdminApp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'AdminApp/UserLoginpage.html')
    else:
        return render(request, 'AdminApp/UserLoginPage.html')





def SignUpSuccessful(request):
    return render(request, 'SignUpSuccessful.html')

"""def LoginHomePage(request):
    return render(request, 'DoctorHomePage.html')"""


def DoctorHomePage(request):
    return render(request, 'DoctorApp/DoctorHomePage.html')


def PatientHomePage(request):
    return render(request, 'PatientApp/PatientHomePage.html')

from .forms import PatientForm
from .models import patient_list

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProjectHomePage')
    else:
        form = PatientForm()
    return render(request, 'adminapp/add_patient.html', {'form': form})


def patient_list(request):
    patients = patient_list.objects.all()
    return render(request, 'adminapp/patient_list.html', {'patients': patients})


