from django.urls import path
from . import views

# app_name = 'login'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
