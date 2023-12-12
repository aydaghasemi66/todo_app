from django.urls import path
from .views import *


app_name = 'todo'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('complete/<int:pk>', CompleteTask.as_view(), name='complete_task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update_task'),
]