from django.urls import path
from . import views

urlpatterns = [
    path("api/cart-list/",views.home,name="cart-list-api"),
    path("cart/",views.cart,name="cart"),
    path("add-to-cart/<product_slug>",views.addtocart,name="add-to-cart"),
    path("remove-from-cart/<product_slug>",views.removefromcart,name="remove-from-cart"),
    ]