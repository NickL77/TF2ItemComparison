import json
from item import Item

with open('backpackTfGetPrices.txt') as json_data:
    d = json.load(json_data)
refMetalWorth = d['response']['raw_usd_value']

items = d['response']['items']
itemSpecs = []

for item in items:
	itemName = item
	print (itemName)
	itemInfo = items[itemName]['prices']
	for qualityInt in itemInfo:
		q = qualityInt
		for tradeVal in itemInfo[q]:
			t = tradeVal
			for craftVal in itemInfo[q][t]:
				c = craftVal	
				if (t != "Tradable" or c != "Craftable"):
					break
				for priceIndex in itemInfo[q][t][c]:
					priceDict = priceIndex
					if type(priceIndex) is dict:
						print (priceIndex['value'])
						
#print(refMetalWorth)

