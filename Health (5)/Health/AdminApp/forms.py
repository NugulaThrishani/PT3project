from django import forms
from .models import Task, patient_list
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title']

class PatientForm(forms.ModelForm):
    class Meta:
        model=patient_list
        fields=['Register_Number','Name']





