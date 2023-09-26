from django.urls import path
from .views import PendingsList, TaskDetail, CreateTask

urlpatterns = [path('', PendingsList.as_view(), name="pendings"),
               path('tasks/<int:pk>', TaskDetail.as_view(), name="tasks"),
               path('create-task/', CreateTask.as_view(), name="create-task")]

