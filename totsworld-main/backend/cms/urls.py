from django.urls import path
from .views import (Inventory,category,Home)
#path('issue_report/',IssueReport,name="issuereport"),
    #path('reviews/',views.Review,name="reviews"),
    #path('edit-product/',Inventory.edit(),name="edit-product"),
    #path('delete-product/',inventory.delete(),name="delete-product"),
    #path('featuredimages/',FeaturedImage.showall(),name="featuredimages"),
    #path('add-featuredimages/',FeaturedImage.showall(),name="featuredimages"),
    #path('edit-featuredimages/',FeaturedImage.showall(),name="featuredimages"),
    #path('featuredimages/',FeaturedImage.delete(),name="featuredimages"),
    #path('banner/',Banner,name="banner"),
    #path('orders/',Order,name="inventory"),
urlpatterns = [
    path('',Home.as_view(),name="dashboard"),
    path('products/',Inventory.showall,name="allproducts"),
    path('add-products/',Inventory.add,name="add-products"),
    path('categories/',category.showall,name="allcategories"),
    path('add-categories/',category.add,name="add-categories"),
    ]
 