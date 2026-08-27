from django.views.generic import TemplateView

class DocumentView(TemplateView):
    template_name = 'about.html'