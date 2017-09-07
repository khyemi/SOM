import json
import pandas as pd
import csv


# get values from JSON file.
with open('nutrients.json', 'r') as fp:
    data = json.load(fp)
"""
#create a sample with 20 foods and 5 nutrients.
print data["Butter, salted"]["Sugars, total"]

a = [[1.2,'abc',3],[1.2,'werew',4],[1.4,'qew',2]]
my_df = pd.DataFrame(a)
my_df.to_csv('my_csv.csv', index=False)

"""

f = csv.writer(open("test.csv", "wb+")))

# write CSV Header
f.writerow(["Protein", "Calcium", "Sugars", "Carbohydrate", "Fat"]
