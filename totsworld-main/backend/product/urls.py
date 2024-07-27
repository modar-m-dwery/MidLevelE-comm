from django.urls import path
from . import views

urlpatterns = [
    path("api/product-list/",views.ProductListAPI,name="product-list"),
    path("products/",views.collection,name="collection"),
    path("collection/<category_slug>/",views.collection,name="products-by-category"),
    path("p/<pslug>/",views.product_detail,name="product_detail"),
    ]