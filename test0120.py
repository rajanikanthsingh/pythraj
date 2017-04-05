#!/usr/bin/python
import os
import urllib2
import xlrd
import urllib
import json
import csv
from xlutils.copy import copy
from xlrd import *
w = copy(open_workbook('sample19.xlsx'))
#rows = []
#output_dir = "."
#filename = "Reportdevicetagvalue_test.csv"
#csv_file = os.path.join(output_dir, filename).encode('utf-8')
#baseurl= 'http://ma-gncstd-lapp08.corp.apple.com:8080/'
#baseurl = 'https://groot-api-ut.corp.apple.com/'
baseurl= 'https://groot-api.apple.com/api/v1/network/'
workbook = xlrd.open_workbook('/Users/raja/Desktop/Workbook2.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
sh1 = workbook.sheet_by_index(0)
sub_attribute_keys = ["Security-Zone","Business-Unit", "Site", "UN-Location-Code"]
for rownum in range(sh1.nrows):
    row_array=sh1.row_values(rownum)
    for ip in row_array:
        try:
           urls = baseurl + ip
           print urls
        # Add your headers
           headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
        # Create the Request
           request = urllib2.Request(urls, None, headers)
        # Getting the response
           response = urllib2.urlopen(request)
           json_obj = response.read()
           data1 = json.loads(json_obj)
           attribute= data1["attributes"]
           #sub_attribute_keys = ["Security-Zone","Business-Unit"]
          # print attribute
           cols = []
           for sub_attrib_key in sub_attribute_keys:
            #sub_attrib_value = attribute.get( sub_attrib_key, "  ")
            sub_attrib_value = attribute.get( sub_attrib_key, [" "])
            #print sub_attrib_value
            cols.append(",".join(sub_attrib_value))
            #w.get_sheet(0).write(0,14,"rows.append(cols)")
            #w.save('book2.xls')
            #cols.append(sub_attrib_value)
            #print cols
            #rows.append(cols)
        except KeyError:
            pass
        #print attribute
        #for item in attribute:
            #try:
                #print ', '.join(attribute["Security-Zone"])
                #print attribute["('\n'.join(Security-Zone))"]
                #print attribute["Business-Unit"]
                #print attribute["Application-Name"]
                #print attribute["Application-ID"]
                #rows.append([','.join(attribute["Security-Zone"]])
                #rows.append([attribute["Security-Zone"],attribute["Business-Unit"],attribute["Application-Name"],attribute["Application-ID"]])
            #except KeyError:
                #pass

#with open(filename, 'wb') as csv_file:
        	#csv_writer = csv.writer(
        	    #csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	#csv_writer.writerows(rows)

            #(str(masterList).translate(string.maketrans('', ''), '[]\'')
