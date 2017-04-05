#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import urllib2
import xlrd
import urllib
import json
import csv
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
rows = []
output_dir = "."
filename = "sitecode18.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')
#baseurl= 'https://capri.corp.apple.com/v1/sites/?site_code='
baseurl= 'http://capri-devweb01.corp.apple.com:8080/v1/sites/?site_code='
workbook = xlrd.open_workbook('/Users/raja/Desktop/Workbook18.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
sh1 = workbook.sheet_by_index(0)
row_array = []
for r in range(0,worksheet.nrows):
    for s in range(0, worksheet.ncols):
        if worksheet.cell_type(r, s) == xlrd.XL_CELL_EMPTY:
            worksheet._cell_values[r][s] = 'NULL'
for rownum in range(sh1.nrows):
    row_array=sh1.row_values(rownum)
    for site in row_array:
           urls = baseurl + site
           print urls
        # Create the Request
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
           request = urllib2.Request(urls, None)
        # Getting the response
           response = urllib2.urlopen(request)
           json_obj = response.read()
           data1 = json.loads(json_obj)
           count = data1['count']
           cols = []
           print count
           if count >= 1:
               #result1 = "1"
               print (count)
               rows.append(['OK'])
           elif count == 0:
               print (count)
               #result0 = "0"
               rows.append(['NA'])
               with open(filename, "wb") as csv_file:
                    csv_writer = csv.writer(
                            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    csv_writer.writerows(rows)


           #for item in data1['results']:
               #print item

               #print sitecode
               #if sitecode == '':
                   #print ('1')
               #else:
                   #print ('0')


                #if count >= 1:
                   #print ('1')
               #else:
                   #print ('0')



           #print data1
           #for item in data1['results']:
               #sitecode= item['site_code']
               #print sitecode