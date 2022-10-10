from django.urls import path
from . import views

urlpatterns = [
    path("map/",views.home, name="home"),
]