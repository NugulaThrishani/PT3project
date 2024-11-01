from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse



# Create your views here.
def ProjectHomePage(request):
    return render(request,'AdminApp/ProjectHomePage.html')

def PatientHomePage(request):
    return render(request, 'PatientApp/PatientHomePage.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import render, redirect
def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')