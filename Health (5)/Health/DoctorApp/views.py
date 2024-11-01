from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def ProjectHomePage(request):
    return render(request,'AdminApp/ProjectHomePage.html')

def DoctorHomePage(request):
    return render(request, 'DoctorApp/DoctorHomePage.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.http import HttpResponseRedirect

def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')