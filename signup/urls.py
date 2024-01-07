from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # include login app URLs
    path('login/', include('login.urls')),
]
