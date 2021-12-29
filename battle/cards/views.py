from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from cards.models import Card

class CardListView(ListView):
    model = Card

class CardDetailView(DetailView):
    model = Card

class CardCreateView(CreateView):
    model = Card
    fields = ['name', 'hp']
    success_url = "/"

class CardUpdateView(UpdateView):
    model = Card
    fields = ['name', 'hp']
    success_url = "/"

class CardDeleteView(DeleteView):
    model = Card
    success_url = "/"
