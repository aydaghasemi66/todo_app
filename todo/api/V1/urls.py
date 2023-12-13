from django.urls import path, include
from .views import *
# from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

# router = DefaultRouter()
# router.register('tasks', TaskView, basename='Tasks')

# urlpatterns = router.urls





urlpatterns = [
    path("tasks/",TaskView.as_view({'get': 'list', 'post':'create'}),name='tasks'),
    path("tasks/<int:pk>",TaskView.as_view({'get': 'retrieve','put':'update','delete': 'destroy'}),name='tasks-detail'),
    
]
