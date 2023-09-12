from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class PendingsList(ListView):
    model = Task
    context_object_name = "tasks"