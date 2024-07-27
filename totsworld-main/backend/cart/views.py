from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from core.models import UserAddress
from .models import Cart
from product.models import Product

# Create your views here.
@api_view(['GET'])
def home(request):
	return HttpResponse(status_code=202)

@login_required(login_url='/signin/')
def cart(request):
    'Show from cart session and db'
    if request.user.is_authenticated:
        try:
            default_address = UserAddress.objects.get(user=request.user,default_address=True)
        except:
            default_address = None
        cart = Cart.objects.filter(user=request.user)
        total_MRP = 0
        discount_price = 0
        coupon_discount = 0
        for i in cart:
            total_MRP += i.get_item_total_price
            discount_price += i.get_item_total_price-((i.get_item_total_price/100)*i.product.sale)
        payable_amount = discount_price - coupon_discount
        context = {
        'cart':cart,
        'total_MRP':total_MRP,
        'discount_price':discount_price,
        'coupon_discount':coupon_discount,
        'payable_amount':payable_amount,
        'default_address':default_address,
        }
        return render(request,'cart.html',context)
    return redirect('signin')

@login_required(login_url='/signin/')
def addtocart(request,product_slug):
    'create a cart session'
    if request.method =="POST":
        user = User.objects.get(username=request.user)
        product = Product.objects.get(slug=product_slug)
        next = request.POST.get('next', '/')
        newtocart = Cart.objects.create(user=user,product=product)
        if newtocart != None:
            newtocart.save()
            messages.success(request,'Added to cart,Procced to checkout?')
            return redirect(next)
        else:
            messages.error(request,'Error Occured')
            return redirect(next)
    return HttpResponse("<h1>Add to cart Page</h1>",status=201)

@login_required(login_url='/signin/')
def removefromcart(request,product_pk):
    if request.method =="POST":
        product = Product.de
    date = datetime.datetime.now()
    return HttpResponse("<h1>remove from cart Page</h1><p>{}</p>".format(date),status=201)