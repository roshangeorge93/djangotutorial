from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("<int:employee_id>/", views.employees, name="employees"),
    path("", views.index, name="index")
]