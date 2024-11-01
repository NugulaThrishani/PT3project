from django.contrib.auth import authenticate
from django.shortcuts import render

#create your views
from django.shortcuts import render
from django.shortcuts import render, redirect

from.forms import TaskForm
from .models import Task



def ProjectHomePage(request):
    return render(request,'adminapp/ProjectHomePage.html')
# Create your views here.
def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User_input: {user_input}')
    a1= {'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)
def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')
def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result=None
        error_message=None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_message=str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})
    return render(request,'adminapp/ExceptionExample.html')
import random
import string
def randompagecall(request):
    return render(request,'adminapp/RandomExample.html')
def randomlogic(request):
    if request.method == "POST":
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1= {'ran':ran}
    return render(request,'adminapp/RandomExample.html',a1)
def calculatepagecall(request):
    return render(request,'adminapp/Calculator.html')
def calculatelogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/Calculator.html', {'result': result})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
def add_task(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
    tasks=Task.objects.all()
    return render(request,'adminapp/add_task.html',{'form':form,'tasks':tasks})
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('add_task')

def register(request):
    return render(request, 'adminapp/UserRegisterPage.html')


def login(request):
    return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')

from datetime import datetime, timedelta
from django.shortcuts import render


def datetimepagecall(request):
    return render(request, 'adminapp/datetime.html')

def datetimepagelogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        a1 = {'ran': ran}
        return render(request, 'adminapp/datetime.html', a1)
    else:
        return render(request, 'adminapp/datetime.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
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
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
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
                return redirect('ProjectHomePage')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegister.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')
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
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as facultyapp!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your facultyapp homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or facultyapp criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')
    else:
        return render(request, 'adminapp/UserLoginPage.html')

from .forms import StudentForm
from .models import StudentList


from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student list')
    else:
        form = StudentForm()

    return render(request, 'adminapp/AddStudent.html', {'form': form})

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ProjectHomePage')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/AddStudent.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student list.html', {'students': students})



from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
from .forms import UploadFileForm  # Assuming you have a form to handle file uploads


def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']

        # Reading CSV file into a pandas DataFrame
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculating total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Extracting month from the 'Date' column
        df['Month'] = df['Date'].dt.month

        # Grouping by month and summing sales
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Mapping month numbers to month names
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        # Creating the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        # Saving the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        # Rendering the template with the chart and sales data
        return render(request, 'adminapp/chart.html', {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })


    # Handle GET request, return the file upload form
    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})


def feedback(request):
    return render(request,'adminapp/feedback.html')

from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or feedback form

    else:
        form = FeedbackForm()  # Create a new form instance

    return render(request, 'feedback_form.html', {'form': form})
    return redirect('success')

def contact_manager(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:contact_manager')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/contact_manager.html', {'form': form, 'tasks': tasks})

# def delete_manager(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect('facultyapp:add_blog')






