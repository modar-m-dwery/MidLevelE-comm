from .models import Cart
from product.models import Product

class Cart:
	"""docstring for Cart"""
	def __init__(self,request):
		self.session = request.session
		cart = sef.session.get('cart')
		if not cart:
			cart = self.session['cart']={}
		self.cart = cart

	def add(self,product,quantity=1,update_quantity=False):
		product_id = product.pk
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0,'price':product.price}
		if update_quantity == True:
		    self.cart['product_id']['quantity']=quantity
		else:
		    self.cart['product_id']['quantity']+=quantity 
		self.save()

	def remove(self,product):
		product_id = product.pk
		if product_id in self.cart:
			del self.cart[product_id]
		    self.save()

	def save(self):
		self.session['cart'] = self.cart
		self.session.modified = True

	def clear(self):
		del self.session['cart']
		self.session.modified = True

	def join_cart(self):
		cart.clear()

	def __iter__(self):
		pass

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(item['quantity']*item['price'] for item in self.cart.values())