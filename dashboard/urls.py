from django.urls import path
from . import views

# app_name = 'login'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    # path('update_profile/', views.update_profile, name='update_profile'),
]
