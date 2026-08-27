from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SighnupView(CreateView):
    template_name = 'registration/sighnup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm