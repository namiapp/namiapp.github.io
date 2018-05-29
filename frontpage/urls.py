from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'frontpage'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
]