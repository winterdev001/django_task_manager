from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path('create', views.TaskCreateView.as_view(), name='create'),
    path('detail/<int:task_id>/', views.TaskDetailView.as_view(), name='detail'),
    path('edit/<int:task_id>/', views.TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:task_id>/', views.TaskDeleteView.as_view(), name='delete')
    
]