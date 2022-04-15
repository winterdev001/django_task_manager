import datetime
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class TaskItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=255)
    deadline = models.DateField(validators=[MinValueValidator(datetime.date.today,message='Deadline must start from today')], blank=False)
    
    def __str__(self):
        return f"title:{self.title}, due:{self.deadline}, status:{self.status}"
    
    # clean data before save
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)