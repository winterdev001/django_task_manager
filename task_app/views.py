from .models import TaskItem
from .forms import TaskForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
class TaskListView(ListView):
    model = TaskItem
    template_name = "task_app/index.html"
    context_object_name = 'task_lists'
    
class TaskCreateView(CreateView):
    model = TaskItem
    template_name = 'task_app/create.html'
    # fields = '__all__'
    form_class = TaskForm
    success_url = reverse_lazy('index')
    
class TaskDetailView(DetailView):
    model = TaskItem
    template_name = "task_app/detail.html"
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

class TaskUpdateView(UpdateView):
    model = TaskItem
    # fields = '__all__'
    form_class = TaskForm
    template_name = "task_app/edit.html"
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    def get_success_url(self):
        return reverse('detail', kwargs={'task_id':self.object.pk})
    
class TaskDeleteView(DeleteView):
    model = TaskItem
    template_name = 'task_app/delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    
