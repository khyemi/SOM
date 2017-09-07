import json
import requests
import urllib2
import csv
import pandas as pd
from itertools import product

  
#store food items from nutrients.json to a list. 
data = []
with open("./nutrient-db-master/nutrients.json") as f:
    for line in f:
      data.append(json.loads(line))

#get nutrients (standard release nutrients only).
nutrientListURL = "https://api.nal.usda.gov/ndb/list?format=json&lt=nr&sort=n&max=1500&api_key=DFn5S4AbjUPdNBUYCL62uTl5aTZLE8RAPtfvHtH0"
nutrientListPage = urllib2.urlopen(nutrientListURL)
nutrients_dict = json.loads(nutrientListPage.read())

foodList = []   #create a list of all food names. 
nutrientList = []   #create a list of all nutrient names.

for row, i in product(data, range(150)):
    foodList.append(row["name"]["long"])
    nutrientList.append(nutrients_dict["list"]["item"][i]["name"])

zero = [0]  
nutrientsValList = zip(nutrientList, zero*150)    #list of nutrients with value 0.

#create a dictionary that stores food names and nutrients. 
nutrientDB = {}
for food in foodList:
  nutrientDB[food] = nutrientsValList

for f_name, n_list in nutrientDB.iteritems():
	for row in data:
		if f_name == row["name"]["long"]:
			#food name matched
			for (nutrient_key, zero_val) in n_list:
				for r in row["nutrients"]:
					if nutrient_key == r["name"]:
						#nutrient name matched
						n_list = dict(n_list)   #convert list to dict 
						n_list[r["name"]] = r["value"]
			nutrientDB[f_name] = n_list	#update dictionary with actual nutrient contents.
                          
#save dictionary as json.
with open('nutrients.json', 'w') as fp:
  json.dump(nutrientDB, fp, sort_keys = True, indent = 4)

