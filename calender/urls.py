from django.urls import path
from .views import CalenderView

urlpatterns = [
    path('', CalenderView.as_view(), name='calender')
]