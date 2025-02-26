from django.urls import path
from django.urls import path
from . import views
from .views import parents, product_list

urlpatterns = [
    path('categories/', parents, name='parents'),
    path("<int:product_id>/", views.product_details, name="product_details"),
    
    path('', product_list, name='product_list'),
]