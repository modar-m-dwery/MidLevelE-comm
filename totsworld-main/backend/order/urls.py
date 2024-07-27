from django.urls import path
from . import views

urlpatterns = [
    path("api/order-list",views.home,name="order-list-api"),
    path('',views.orders,name="orders"),
    ]