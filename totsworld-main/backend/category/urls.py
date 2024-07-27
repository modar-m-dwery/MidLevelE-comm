from django.urls import path
from . import views

urlpatterns = [
    path("api/category-list",views.home,name="category-list-api"),
    ]