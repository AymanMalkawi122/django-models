from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Snack
# Create your views here.

class SnacksListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = "snacks"

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack
