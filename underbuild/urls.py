from . import views
from django.urls import path
from land import views as land

urlpatterns = [
    path('home/', land.home, name='home'),  
]