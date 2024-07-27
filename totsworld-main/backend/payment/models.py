from django.db import models
from order.models import Order
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
	pay_choices = (('upi','UPI'),('card','Card'),('netbanking','Net Banking'))
	transaction_id = models.CharField(max_length=50)
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	payment_method = models.CharField(choices=pay_choices,max_length=50)
	amount = models.FloatField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.transaction_id