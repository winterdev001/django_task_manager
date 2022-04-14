from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from .models import TaskItem

# Create your views here.
class TaskListView(ListView):
    model = TaskItem
    template_name = "task_app/index.html"