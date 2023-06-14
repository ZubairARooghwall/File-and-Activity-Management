from django.urls import path
from . import views

urlpatterns = [
	# Everything homepage
	path('', views.home, name="home"),
	path('settings', views.settings, name='settings'),
	path('statistics', views.statistics, name='statistics'),
	
	
	
	
	
]