from django.urls import path
from . import views

urlpatterns = [
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
]