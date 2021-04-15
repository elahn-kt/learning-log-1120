

"""Defines URL patterns for users"""
from django.contrib import admin

from django.urls import path
#from django.conf.urls import url
#from django.contrib.auth.views import login
#from django.contrib.auth import login
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
	# Login page
#	path(r'login/', login, {'template_name': 'users/login.html'}, name='login'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	
	# Logout page
	path(r'logout/', views.logout_view, name='logout'),
#	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

	# Registration page
	path(r'register/', views.register, name='register'),
]
