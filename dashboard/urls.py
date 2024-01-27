from django.urls import path
from .views import dashboard, update_profile

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('update_profile/', update_profile, name='update_profile'),
    # Add other URL patterns as needed
]