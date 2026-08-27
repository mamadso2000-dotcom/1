from django.urls import path
from .views import PlansView

urlpatterns = [
    path('', PlansView.as_view(), name='plans')
]