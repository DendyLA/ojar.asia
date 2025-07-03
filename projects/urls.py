from django.urls import path
from . import views

urlpatterns = [
	path( 'current-projects/', views.projectsCurrent, name='current-projects'),
	path( 'not-current-projects/', views.projectsNotCurrent, name='not-current-projects'),
	path( '<slug:slug>/', views.projectsDetail, name='projects-detail')
]
