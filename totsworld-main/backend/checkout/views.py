import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core.models import Review,UserAddress,FeaturedImage,Banner
from cart.models import Cart
from order.models import Order,ProductOrder
from category.models import Category
from payment.models import Payment
from product.models import Product
from django.contrib.auth.models import User
from .checkout import Checkout
from product.recent import RecentProduct

# Create your views here.
@login_required(login_url='/signin/')
def checkout(request):
    if request.method == 'POST':
        '''create a checkout session'''
        checkout = Checkout(request)
        checkout_id = settings.CHECKOUT_SESSION_ID

        if checkout_id is None:
            settings.CHECKOUT_SESSION_ID = request.session.id
        address_id = request.POST.get('addressid')
        adr = UserAddress.objects.get(pk=address_id)
        checkout.addaddress(adr)
        return redirect('checkout-payment')

    elif request.method == 'GET':
        cart = Cart.objects.filter(user=request.user)
        if cart is not None:
            options = UserAddress.objects.filter(user=request.user)
            #total_MRP = 0
            discount_price = 0
            coupon_discount = 0
            for i in cart:
                #total_MRP += i.get_item_total_price
                discount_price += i.get_item_total_price-((i.get_item_total_price/100)*i.product.sale)
            payable_amount = discount_price - coupon_discount
            context = {
            'options':options,
            'cart':cart,
            'total':payable_amount,
            }
            return render(request,'checkout.html',context)
        else:
            messages.error('Your Cart is Empty')
            return redirect('cart')
    else:
        return HttpResponse(status=400)

@login_required(login_url='/signin/')
def payment(request):
    checkout = Checkout(request)
    if request.method == "POST":
        payment_method = request.POST.get('payment_method')
        checkout.make_payment(payment_method)
        return redirect('proceed-to-pay')
    return render(request,'payment.html')

@login_required(login_url='/signin/')
def proceed_topay(request):
    checkout = Checkout(request)
    checkout.confirm_payment

    order = Order.objects.create(
        order_uniqid="order_12345",
        user=request.user,
        address=UserAddress.objects.get(pk=checkout.checkout['address']['address_id']),
        payment_status="successful",
        order_status="successful",
        )
    order.save()
    cart = Cart.objects.filter(user=request.user)
    for item in cart:
        new = ProductOrder.objects.create(
            product=item.product,
            order=order,
            quantity=1,
            order_status='successful',
            )
        new.save()
        item.delete()
    pay = Payment.objects.create(
        transaction_id="tp_1010",
        order=order,
        user=request.user,
        payment_method='',
        amount=0,
        )
    checkout.clear()
    return render(request,'proceed.html',{'order_status':order.order_status})