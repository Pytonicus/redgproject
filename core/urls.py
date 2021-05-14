from django.urls import path 
from . import views as core

urlpatterns = [
    path('', core.home, name='home'),
    path('login/', core.iniciar_sesion, name='login')
]