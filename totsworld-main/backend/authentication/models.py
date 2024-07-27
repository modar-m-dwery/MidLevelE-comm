from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    #password = models.TextField(max_length=50)
    username = models.CharField(max_length=15,null=True)
    fullname = models.CharField(max_length=50,null=True)
    email =models.EmailField(null=True,max_length=30)
    phone = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.fullname
