from product.models import Product

class RecentProduct(object):
	def __init__(self,request):
		self.session = request.session
		recent_products = self.session.get('recent_products')
		if not recent_products:
			recent_products = self.session['recent_products'] = {}
		self.recent_products = recent_products
	def add(self,product):
		product_id = str(product.id)
		if product_id not in self.recent_products:
			self.recent_products[product.id] = {}
		self.save()
	def save(self):
		self.session['recent_products'] = self.recent_products
		self.session.modified=True
	def clear(self):
		del self.session['recent_products']
		self.session.modified = True
	def __iter__(self):
		if self.recent_products:
			product_ids = self.recent_products.keys()
			products = Product.objects.filter(pk__in=product_ids)
			for product in products:
				self.recent_products[str(product.id)]['product'] = product
			for item in self.recent_products.values():
				yield item