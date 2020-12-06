class MyBikk(object):
	def __init__(self,speed,cc,price):
		self.speed=speed
		self.cc=cc
		self.price=price
	def Details(self):
		print "Speed:",self.speed
		print "CC:",self.cc
		print "Price:",self.price

Bikk=MyBikk("180km/hr","180","1.20Lac")
Bikk.Details()

