from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class patient_list(models.Model):
    Register_Number=models.CharField(max_length=20,unique=True)
    Name=models.CharField(max_length=100)

    def _str_(self):
        return self.Register_Number