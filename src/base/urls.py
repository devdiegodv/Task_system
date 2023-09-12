from django.urls import path
from .views import PendingsList

urlpatterns = [path('', PendingsList.as_view(), name="pendientes")]

