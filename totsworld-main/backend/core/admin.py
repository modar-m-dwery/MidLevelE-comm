from django.contrib import admin
from .models import (UserAddress,ReportIssue,Setting,Review,
    Referral,Banner,FeaturedImage)
#Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['fullname','user','pin','default_address','created_at']
admin.site.register(UserAddress,UserAddressAdmin)
#admin.site.register(Payment)
admin.site.register(ReportIssue)
admin.site.register(Setting)
admin.site.register(Review)
#admin.site.register(Wishlist)
admin.site.register(Referral)
admin.site.register(Banner)
admin.site.register(FeaturedImage)