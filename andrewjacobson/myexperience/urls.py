from django.urls import path
from . import views

urlpatterns = [
    path("", views.myexperience_index, name="myexperience_index"),
]