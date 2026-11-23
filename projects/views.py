from django.views.generic import ListView, DetailView
from .models import Project

class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project

class ProjectDetailView(DetailView):
    template_name = 'projectdetail.html'
    model = Project
    context_object_name = 'project'