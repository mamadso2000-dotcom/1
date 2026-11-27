from django.urls import path
from .views import (AstronomyView,
                    GalleryView,
                    CalendarView,
                    PlansView,
                    Planet_Detail,
                    CalendarDayView,
                    PlanDetailView
                    )

urlpatterns = [
    path('', AstronomyView.as_view(), name='astronomy'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("calendar/<int:year>/<int:month>/", CalendarView.as_view(), name="calendar_month"),
    path("calendar/<int:year>/<int:month>/<int:day>/", CalendarDayView.as_view(), name="calendar_day"),
    path("plans/", PlansView.as_view(), name="plans"),
    path("plans/<int:event_id>/", PlanDetailView.as_view(), name="plan_detail"),
    path("planets/<int:pk>/", Planet_Detail.as_view(), name="planet_detail"),
]