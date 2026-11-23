from django.urls import path
from .views import ProgramsView

urlpatterns = [
    path('', ProgramsView.as_view(), name='programs')
]