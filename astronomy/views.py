from django.views.generic import ListView, DetailView
from .models import Planet

# moder views
class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Planet

class CalenderView(ListView):
    template_name = 'calender.html'
    model = Planet

class PlansView(ListView):
    template_name = 'plans.html'
    model = Planet

# son views
class Planet_Detail(DetailView):
    template_name = 'planet_detail.html'
    model = Planet