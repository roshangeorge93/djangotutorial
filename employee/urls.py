from django.urls import include, path
from . import views

urlpatterns = [
    path("<int:em_id>/", views.detail, name='detail'),
    path("", views.index, name="index")
]

