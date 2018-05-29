from django.contrib import admin
from django.urls import path, include

from . import views

admin.autodiscover()

app_name = 'mapper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
	# authentication URLS
	path('signup/', views.SignUp.as_view(), name='signup'),
]