from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Order

# Create your views here.
@api_view(['GET'])
def home(request):
	return HttpResponse(status_code=202)

@login_required(login_url='/signin/')
def orders(request):
    orders = Order.objects.filter(user=request.user)
    #product = ProductOrder.objects.filter(order=orders.pk)
    return render(request,'orders.html',{'orders':orders,})