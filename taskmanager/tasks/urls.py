from django.urls import path
from .views import TaskListCreateAPIView, TaskUpdateDeleteAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskUpdateDeleteAPIView.as_view(), name='task-update-delete'),
]
