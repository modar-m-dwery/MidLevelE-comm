from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'home.html')
def landing_page2(request):
    return render(request, 'home2.html')


def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')