from django.urls import include, path
from . import views

urlpatterns = [
    path("<int:pr_id>/", views.product_detail, name='product_detail'),
    path("", views.product_index, name="product_index"),
    path("categories/", views.categories, name="categories")

]