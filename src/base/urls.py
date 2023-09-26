from django.urls import path
from .views import PendingsList, TaskDetail, CreateTask, EditTask, DeleteTask

urlpatterns = [path('', PendingsList.as_view(), name="tasks"),
               path('tasks/<int:pk>', TaskDetail.as_view(), name="task"),
               path('create-task/', CreateTask.as_view(), name="create-task"),
               path('edit-task/<int:pk>', EditTask.as_view(), name="edit-task"),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name="delete-task")]