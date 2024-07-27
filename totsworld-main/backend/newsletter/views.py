from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt
from .models import Newsletter
from .serializers import NewsletterSerializer

from .models import Newsletter
# Create your views here.
@api_view(['POST'])
def subscribe(request):
	if request.method=="POST":
		new = NewsletterSerializer(data=request.data)
		if new.is_valid():
			new.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=202)
	else:
		return HttpResponse(status=400)
"""
@api_view(['GET','POST'])
def unsubscribe(request,pk):
	subscriber = Newsletter.objects.get(pk=pk)
	if request.method=="POST":
		new = NewsletterSerializer(instance=subscriber,data=request.data)
		if new.is_valid():
			new.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=202)
	elif request.method=="GET":
		serializer = NewsletterSerializer(subscriber,many=False)
		return Response(serializer.data)
	else:
		return HttpResponse(status=400)
"""
def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        nextpage = request.POST.get('next')
        if Newsletter.objects.filter(email=email) == None:
            subscribe = Newsletter.objects.create(email=email,subscription_status=True)
            subscribe.save()
            messages.success(request,'Thanks for subscribing to our newsletter!')
            return redirect(nextpage)
        else:
            messages.info(request,'You have already subscribed, Thanks!')
            return redirect(nextpage)
    messages.info(request,'Bad Request!')
    return HttpResponse("<h1>Bad Request</h1>",status=201)