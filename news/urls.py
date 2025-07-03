from django.urls import path
from . import views

urlpatterns = [
	path('', views.news, name='news-all'),
	path('<slug:slug>/', views.newsDetail, name='news-detail')
]
