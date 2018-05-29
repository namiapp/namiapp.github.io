from django.db import models
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'frontpage/index.html'

class AboutView(generic.TemplateView):
	template_name = 'frontpage/about.html'
