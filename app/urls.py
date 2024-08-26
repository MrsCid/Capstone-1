from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name='index'),
    path('placa/',placa,name='placa'),
    path('registro/', RegisterView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    ]