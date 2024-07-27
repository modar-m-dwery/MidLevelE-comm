from django.contrib import admin
from .models import Newsletter
# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('pk','email','subscription_status','created_at','updated_at')
admin.site.register(Newsletter,NewsletterAdmin)