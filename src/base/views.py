from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class PendingsList(ListView):
    '''
    Show a list ob tasks (objects)
    '''
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    '''
    Show one task detail
    '''
    model = Task
    context_object_name = 'task'
    template_name = "base/task_detail.html"

class CreateTask(CreateView):
    '''
    Create new tasks
    '''
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class EditTask(UpdateView):
    '''
    Edit a task
    '''
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    '''
    Delete a task
    '''
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')