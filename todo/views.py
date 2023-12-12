from django.shortcuts import get_object_or_404, redirect
from accounts.models import CustomeUser
from django.views.generic import ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import *



class HomeView(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    
    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = self.request.user
            task.save()
            return redirect('/')


class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/'


class CompleteTask(LoginRequiredMixin, View):
    model = Task
    success_url = '/'
    fields = ['title']


class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/update_task.html'
    fields = ['title']
    success_url = '/'
    context_object_name = 'task'
