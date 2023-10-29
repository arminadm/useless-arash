from django.shortcuts import render
from django.views.generic import TemplateView


class indexview(TemplateView):
    template_name = "index.html"