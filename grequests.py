#!/usr/bin/python
import os
import urllib2
import xlrd
import urllib
import json
import csv
rows = []
output_dir = "."
filename = "newtagvalue.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')
baseurl= 'https://groot-api.apple.com/api/v1/network/'
workbook = xlrd.open_workbook('/Users/raja/Desktop/Workbook1.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
sh1 = workbook.sheet_by_index(0)
row_array = []
#print "content of", sh1.name
for rownum in range(sh1.nrows):
    #print sh1.row_values(rownum)
    row_array=sh1.row_values(rownum)
    #print row_array
    for ip in row_array:
        urls = baseurl + ip
        print ip
        # Add your headers
        headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
        # Create the Request
        request = urllib2.Request(urls, None, headers)
        # Getting the response
        response = urllib2.urlopen(request)
        json_obj = response.read()
        data1 = json.loads(json_obj)
        attribute= data1["attributes"]
        #print attribute
        rows.append([data1["attributes"]])
        #for item in attribute:
            #try:
                #print attribute["Security-Zone"]
                #print attribute["Business-Unit"]
                #print attribute["Application-Name"]
                #print attribute["Application-ID"]
                #rows.append([attribute["Security-Zone"]])
            #except KeyError:
                #pass
        #print attribute["Security-Zone"]
        #print attribute
#rows = []
#output_dir = "."
#filename = "tagvalue.csv"
#csv_file = os.path.join(output_dir, filename).encode('utf-8')
#rows.append([attribute["Security-Zone"]])
#rows.append([row_array["ip"],attribute["Security-Zone"],attribute["Business-Unit"],attribute["Application-Name"],attribute["Application-ID"],data1["attributes"]])
with open(filename, "wb") as csv_file:
        	csv_writer = csv.writer(
        	    csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	csv_writer.writerows(rows)
#num_rows = worksheet.nrows - 1
#curr_row = 0
#cells = worksheet.row_slice(rowx=0, start_colx=0,end_colx=2)
#for cell in cells:
    #print cell.value
#cell = worksheet.cell(0,0)

#print cell.value
#creates an array to store all the rows
#row_array = []

#while curr_row < num_rows:
    #row = worksheet.row(curr_row)
    #row_array += row
    #curr_row += 1

#print row_array
#ips = row_array
#print ips
##for text in ips:
    #print text

    #urls = baseurl + ip
    #print urls
