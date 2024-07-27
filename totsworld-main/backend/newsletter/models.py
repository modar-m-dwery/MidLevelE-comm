from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.CharField(max_length=50)
    subscription_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email