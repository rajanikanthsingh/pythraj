#!/usr/bin/python
import os
import requests
import json
import csv
url='http://ma-gncstd-lapp08.corp.apple.com:8080/api/v1/networks/search/'
filter = """
#{
##"entries": {
# "view_count": 100,
#{"filters":{"attributes": {"Site":[Cupertino]}}}
{"filters":{"attributes": {"Region":[ "AMR"]}}}
}
"""
#headers = {'content-type': 'application/json'}
#r = requests.post(url, data=json.dumps(filter), headers=headers)
r = requests.post ('http://ma-gncstd-lapp08.corp.apple.com:8080/api/v1/networks/search/', params="filter")
#params="filter")
data = r.json()
print data
#output_dir = "."
#filename = "postquery.csv"
#csv_file = os.path.join(output_dir, filename)


#rows = []
for item in data['entries']:
#       rows.append([item['id'],item['network_type'], item["attributes"] ])
        #print item['id']
        #print item['network_type']
      print item["attributes"]
   

#with open(filename, "wb") as csv_file:
#	csv_writer = csv.writer(
#        csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL
#    )
#	csv_writer.writerows(rows)

#if 'Region' in data['entries']:
#	print data["attributes"]["Region"]
#	print Region
