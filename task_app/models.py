import datetime
from email.policy import default
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class TaskItem(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(null=False)
    status = models.CharField(max_length=255, null=False)
    deadline = models.DateField(validators=[MinValueValidator(datetime.date.today)], default=datetime.date.today)
    
    def __str__(self):
        return f"{self.title}: due{self.deadline}, status:{self.status}"