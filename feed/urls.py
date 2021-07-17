from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.feed, name="feed"),
	path('post-save/', views.post_save, name="post_save"),
	
	path('post-details/<str:post_id>/', views.post_details, name="post_details"),
]