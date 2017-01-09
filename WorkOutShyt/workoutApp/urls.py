from django.conf.urls import patterns, url
from workoutApp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'), 
	url(r'^about/', views.about, name='about'),
	url(r'^exercise/(?P<exercise_name>[\w\-]+)/$', views.exercise, name='exercise'),
	#url(r'^profile/),


		)