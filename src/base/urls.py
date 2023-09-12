from django.urls import path
from .views import PendingsList, TaskDetail

urlpatterns = [path('', PendingsList.as_view(), name="pendings"),
               path('tasks/<int:pk>', TaskDetail.as_view(), name="tasks")]

