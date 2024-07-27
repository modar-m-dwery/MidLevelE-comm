#from shop.models import Order,UserAddress

class Checkout:
	def __init__(self,request):
		self.session = request.session
		checkout = self.session.get('checkout')
		if not checkout:
			checkout = self.session['checkout']= {}
		self.checkout = checkout

	def save(self):
		self.session['checkout'] = self.checkout
		self.session.modified = True

	def clear(self):
		del self.session['checkout']
		self.session.modified = True

	def addaddress(self,address):
		address_id = str(address.id)
		self.checkout['address']={'address_id':address_id,}
		self.save()

	def make_payment(self,payment):
		payment_method = str(payment)
		self.checkout['payment']={'payment_method':payment_method,'payment_status':'pending'}
		self.save()

	@property
	def confirm_payment(self):
		self.checkout['payment']['payment_status']='successful'
		self.save()
