from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET'])
def home(request):
	return HttpResponse(status_code=202)