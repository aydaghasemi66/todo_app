from django.urls import path, include
from .views import *



app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('Complete/<int:pk>', CompleteTask.as_view(), name='complete_task'),
    path("api/V1/",include('todo.api.V1.urls')),
]