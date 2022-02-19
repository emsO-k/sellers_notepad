from django.forms import ModelForm, widgets
from django import forms
from django.utils import timezone
from .models import Task, Client


class TaskForm(ModelForm):
    # due_date = forms.DateField(
    #     label=f'Fecha: {Task.default_date().strftime("%d/%m/%Y")}', widget=forms.DateInput(attrs={"type": "date"}), initial=Task.default_date(), required=False)
    new_client = forms.CharField(
        max_length=100, label="Cliente nuevo", required=False)

    class Meta:
        model = Task
        fields = ["client", "description"]
        labels = {
            "client": "Cliente",
            "description": "Notas",
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['client'].required = False
        # field_classes = {
        #     "description": "style"
        # }
        # help_texts = {
        #     "description": "Pone algo aca"
        # }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            "name": "Nombre",
            "address": "Dirección"
        }
