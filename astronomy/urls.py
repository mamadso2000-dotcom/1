from django.urls import path
from .views import (GalleryView,
                    CalendarView,
                    PlansView,
                    Planet_Detail)

urlpatterns = [
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('plans/', PlansView.as_view(), name='plans'),
    path("planets/<int:pk>/", Planet_Detail.as_view(), name="planet_detail"),
]