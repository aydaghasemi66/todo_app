from django.urls import path
from .views import *



app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('Complete/<int:pk>', CompleteTask.as_view(), name='edit_task'),
]