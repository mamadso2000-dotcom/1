from django.urls import path
from .views import SighnupView

urlpatterns = [
    path('sighnup/', SighnupView.as_view(), name='sighnup')
]