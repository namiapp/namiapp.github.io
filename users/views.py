from django.db import models
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class HomeView(generic.TemplateView):
	template_name = 'users/home.html'

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/signup.html'