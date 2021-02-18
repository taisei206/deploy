from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here.



class HomeView(TemplateView):
    template_name = "tweet/Home.html"

