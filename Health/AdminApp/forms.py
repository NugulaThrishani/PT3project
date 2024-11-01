from django import forms
from .models import Task, patient_list
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title']

# AdminApp/models.py

from django.db import models

class PatientList(models.Model):
    register_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    # Add other relevant fields here

    def __str__(self):
        return f"{self.register_number} - {self.name}"

    class Meta:
        db_table = 'AdminApp_patient_list'
        abstract = True





