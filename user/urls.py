from django.urls import path
from . import views

urlpatterns = [
	path('account/info/', views.account_info, name="account_info"),
	path('account/settings/', views.account_settings, name="account_settings"),
	path('user-profile/<str:user_id>', views.user_profile, name="user_profile"),

]