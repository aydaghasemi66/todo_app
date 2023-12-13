from rest_framework.response import Response
from .serializer import *
from ...models import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class TaskView(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    

    def list(self, request, *args, **kwargs):
        tasks_serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(tasks_serializer.data)
    def retrieve(self, request, *args, **kwargs):
        tasks = get_object_or_404(self.get_queryset(), pk=kwargs.get('pk'))
        tasks_serializer = self.serializer_class(tasks)
        return Response(tasks_serializer.data)
        
    def create(self, request, *args, **kwargs):
         tasks_serializer = self.serializer_class(data=request.data)
         tasks_serializer.is_valid(raise_exception=True)
         tasks_serializer.save()
         return Response(tasks_serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        task = get_object_or_404(self.get_queryset(), pk=kwargs.get('pk'))
        task.delete()
        return Response("Task deleted successfully")
    
    def update(self, request, *args, **kwargs):
        task = get_object_or_404(self.get_queryset(), pk=kwargs.get('pk'))
        task_serializer = self.serializer_class(task, data=request.data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save()
        return Response(task_serializer.data)
