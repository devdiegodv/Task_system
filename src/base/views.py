from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

class Login(LoginView):
    '''
    Login logic
    '''
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class PendingsList(LoginRequiredMixin, ListView):
    '''
    Show a list ob tasks (objects)
    '''
    model = Task
    context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
    '''
    Show one task detail
    '''
    model = Task
    context_object_name = 'task'
    template_name = "base/task_detail.html"

class CreateTask(LoginRequiredMixin, CreateView):
    '''
    Create new tasks
    '''
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class EditTask(LoginRequiredMixin, UpdateView):
    '''
    Edit a task
    '''
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    '''
    Delete a task
    '''
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')