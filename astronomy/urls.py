from django.urls import path
from .views import (GalleryView,
                    CalenderView,
                    PlansView,
                    Planet_Detail)

urlpatterns = [
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('calender/', CalenderView.as_view(), name='calender'),
    path('plans/', PlansView.as_view(), name='plans'),
    path("planets/<int:pk>/", Planet_Detail.as_view(), name="planet_detail"),
]