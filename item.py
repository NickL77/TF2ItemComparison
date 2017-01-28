class Item(object):
	def __init__(self, qualityInt, name, currency, value, keyWorth):
		self.name = name
		self.value = value
	def getName (self):
		print self.name
	def getValue(self):
		print self.value
