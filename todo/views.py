from django.shortcuts import get_object_or_404, redirect
from accounts.models import CustomeUser
from django.views.generic import ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import CreateTaskForm



class HomeView(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        pass

    
    def post(self, request, *args, **kwargs):
        pass




class DeleteTask(DeleteView):
    model = Task
    success_url = '/'





class CompleteTask(LoginRequiredMixin, View):
    pass



class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/update_task.html'
    fields = ['title']
    success_url = '/'
    context_object_name = 'task'
