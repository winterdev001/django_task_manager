from django import forms
from .models import TaskItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = '__all__'        
        pulldown_data = [
            ("todo","todo"),
            ("doing","doing"),
            ("done","done"),
        ]
        widgets = {
            'description': forms.Textarea(),
            'status': forms.Select(choices=pulldown_data),
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
