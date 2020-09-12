from . import views
from django.urls import path
from myfolio import views as myfolio
from underbuild import views as underbuild

urlpatterns = [
    path('', views.home, name="home"),
    path('porto/', myfolio.home, name="porto"),
    path('apps/', underbuild.home, name="apps"),
]