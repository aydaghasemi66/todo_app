from .serializer import *
from ...models import *
from rest_framework import viewsets



class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
