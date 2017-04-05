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
filename = "tagvalue3.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')
baseurl= 'https://groot-api.apple.com/api/v1/network/'
workbook = xlrd.open_workbook('/Users/raja/Desktop/Workbook2.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
sh1 = workbook.sheet_by_index(0)
row_array = []
for rownum in range(sh1.nrows):
    row_array=sh1.row_values(rownum)
    for ip in row_array:
        try:
           print ip
           urls = baseurl + ip
        # Add your headers
           headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
        # Create the Request
           request = urllib2.Request(urls, None, headers)
        # Getting the response
           response = urllib2.urlopen(request)
           json_obj = response.read()
           data1 = json.loads(json_obj)
           attribute= data1["attributes"]
           print attribute["Security-Zone"]
        #print '[%s]' % ', '.join(map(str,attribute["Security-Zone"]))
           #rows.append([attribute["Security-Zone"]])
        except KeyError:
           pass
        #for index, item in enumerate(attribute):
            #default = 'null'
            #try:
                #SecurityZone = attribute["Security-Zone"]
                #Businessunit = attribute["Business-Unit"]
                #ApplicationName = attribute["Application-Name"]
                #ApplicationID = attribute["Application-ID"]
                #print  SecurityZone
                #print Businessunit
                #print ApplicationName
                #print ApplicationID
            #except KeyError:
                #pass
                #for attribute  in SecurityZone:
                    #sz = item
                   # print attribute
                    #rows.append (["sz"])
                #for unit in Businessunit:
                    #print unit
                    #rows.append[unit['Businessunit']]
                #for name in ApplicationName:
                    #print name
                    #rows.append[name['ApplicationName']]
                #for id in ApplicationID:
                   # print id
                    #rows.append[id['ApplicationID']]

                #rows.append([attribute[SecurityZone], attribute["Businessunit"], attribute["ApplicationName"], attribute["ApplicationID"]])


        with open(filename, "wb") as csv_file:
        	csv_writer = csv.writer(
        	    csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	csv_writer.writerows(rows)

                    #rows.append[','.join["Security-Zone"]])


            #for str in SecurityZone:
                #try:`
                    #str(SecurityZone).translate(string.maketrans('', ''), '[]\'')
                    #print str
                #except KeyError:
                    #pass

            #print ', '.join(map(str, LIST))
            #value = SecurityZone.get["str", None]
            #Business-Unit = attribute["Business-Unit"]
            #Application-Name = attribute["Application-Name"]
            #Application-ID = attribute["Application-ID"]
            #if value is not None:
                   # print '\n'.join(SecurityZone)
                    #pass
                    #print attribute["'\n'.join(Security-Zone)"]
                    #print attribute["Business-Unit"]
                    #print attribute["Application-Name"]
                    #print attribute["Application-ID"]
                    #rows.append([attribute["Security-Zone"],attribute["Business-Unit"],attribute["Application-Name"],attribute["Application-ID"]])
                #except KeyError:
                        #pass

#with open(filename, "wb") as csv_file:
        	#csv_writer = csv.writer(
        	    #csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	#csv_writer.writerows(rows)



#for item in attribute:
            #Security-Zone = attribute["Security-Zone"]
            #Business-Unit = attribute["Business-Unit"]
            #Application-Name = attribute["Application-Name"]
            #Application-ID = attribute["Application-ID"
            #for str in Security-Zone:
                 #try:
                 #print str
                #print attribute["Security-Zone"]
                #print attribute["Business-Unit"]
                #print attribute["Application-Name"]
                #print attribute["Application-ID"]
                #rows.append([attribute["Security-Zone"],attribute["Business-Unit"],attribute["Application-Name"],attribute["Application-ID"]])
            #except KeyError:
                #pass