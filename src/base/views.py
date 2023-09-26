from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

class RegisterPage(FormView):
    '''
    Register logic
    '''
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class PendingsList(LoginRequiredMixin, ListView):
    '''
    Show a list ob tasks (objects)
    '''
    model = Task
    context_object_name = 'tasks'

    '''
    Show user tasks
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] =  context['tasks'].filter(user=self.request.user)
        context['count'] =  context['tasks'].filter(completed=False).count()

        searched_value = self.request.GET.get('search-area') or ''
        if searched_value:
            context['tasks'] = context['tasks'].filter(title__icontains=searched_value)
        context['searched_value'] = searched_value
        return context

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
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    '''
    Asign form to user
    '''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class EditTask(LoginRequiredMixin, UpdateView):
    '''
    Edit a task
    '''
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    '''
    Delete a task
    '''
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')