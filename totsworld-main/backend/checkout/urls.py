from django.urls import path
from . import views

urlpatterns = [
path('checkout/',views.checkout,name="checkout-address"),
path('checkout/payment/',views.payment,name="checkout-payment"),
path('proceed-to-pay/',views.proceed_topay,name="proceed-to-pay")
]