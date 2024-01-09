from django.urls import path, include
from . import views

urlpatterns = [
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('login/', include('login.urls')),
]