from django import forms

class TaskForm(forms.Form):
    pulldown_data = [
        ('1','todo'),
        ('2','doing'),
        ('1','done')
    ]
    
    title = forms.CharField(label='Title')
    desciption = forms.CharField(label='Description', widget=forms.Textarea())
    status = forms.ChoiceField(label='Status', choices=pulldown_data)
    deadline = forms.DateField(label='Deadline')
    