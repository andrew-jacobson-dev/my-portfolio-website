from django.urls import path
from . import views

urlpatterns = [
    path("", views.myprojects_index, name="myprojects_index"),
    path("<int:project_id>/", views.myprojects_detail, name="myprojects_detail"),
]

