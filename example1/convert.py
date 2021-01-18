#!/usr/bin/env python3

import csv
import json

# use csv.DictReader to load input.csv
# create a variable 'rows' with all of the rows in the csv
with open("input.csv", "r") as f:
	reader = csv.DictReader(f)
	rows = list(reader)

#print(rows)

# loop through each row of the input which is in the format
# {
#   'title': ..., 
#   'subtitle': ..., 
#   'range_min': ..., 
#   'range_mid': ..., 
#   'range_max': ..., 
#   'measure_min': ..., 
#   'measure_max': ...
# }

# and transform it into the format

# {
#  'title': ...,
#  'subtitle': ...,
#  'ranges': [...],
#  'measures': [...],
#  'markers': [...],
# }

data = []
for row in rows:
	print(row)
	datapoint = {
		"title": row["title"],
		"subtitle": row["subtitle"],
		"ranges": [
			float(row["range_min"]),
			float(row["range_mid"]),
			float(row["range_max"])],
		"measures": [
			float(row["measure_min"]),
			float(row["measure_max"])],
		"markers": row["markers"]
		}
	data.append(datapoint)

# use json.dump to output, 'output.json'
with open('output.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)




