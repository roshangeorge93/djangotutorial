from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("<int:student_id>/", views.student, name="student"),
    path("", views.student_list, name="student_list")
]