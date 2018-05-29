from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
	# authentication URLS
	path('signup/', views.SignUp.as_view(), name='signup'),
]