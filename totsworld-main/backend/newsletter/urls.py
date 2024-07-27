from django.urls import path
from . import views

urlpatterns = [
    path("newsletter",views.newsletter,name="newsletter"),
    path("subscribe/",views.subscribe,name="subscribe"),
    #path("unsubscribe/<pk>/",views.unsubscribe,name="unsubscribe"),
    ]