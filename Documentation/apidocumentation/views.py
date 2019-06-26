from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView

# Create your views here.
class TestView(TemplateView):
    template_name = "apidocumentation/base.html"
