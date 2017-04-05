#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import urllib2
import urllib
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

filter = """
{
  "data": {
    "page": 1,
    "Type": "Device",
    "Filters": {
      "support_group__name": "GNS Field Services",
      "status_id": "3"
    }
  }
}
"""

devicefilter = """
{
  "data": {
    "page": 1,
    "Type": "DeviceInterface",
    "Filters": {
      "device_id": "3"
    }
  }
}
"""

rows = []
output_dir = "."
filename = "gnsfieldservicesdeviceinterface.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')

filterObj = json.loads(filter)
devicefilters = json.loads(devicefilter)
vartmp = 0
varItr=1;
while True:
    url = 'https://capri.corp.apple.com/v0/query'
    req = urllib2.Request(url, json.dumps(filterObj),)
    response = urllib2.urlopen(req)
    json_obj = response.read()
    data = json.loads(json_obj)
    for item in data['data'] :
        varsa=  item['id']
        print varsa
        devicefilters['data']['Filters']['device_id'] = varsa
        request = urllib2.Request(url, json.dumps(devicefilters),)
        responses = urllib2.urlopen(request)
        json_obj = responses.read()
        deviceinterfacedata = json.loads(json_obj)
        #yourstring = deviceinterfacedata.encode('ascii', 'ignore').decode('ascii')
        #deviceinterfacedata.encode('utf-8')
       #print  deviceinterfacedata
        for deviceinfo in deviceinterfacedata['data']:
		rows.append([deviceinfo['device_name'],deviceinfo['name'],deviceinfo['ip'],deviceinfo['ip_subnet'],deviceinfo['id'],item['snmp_location'],item['fqdn'],item['mgmt_ip'],deviceinfo['description'] ])
	        print deviceinfo['name']
       		print deviceinfo['ip']
       		print deviceinfo['ip_subnet']
       		print deviceinfo['id']
       		print deviceinfo['device_name']
        	print item['snmp_location']
               	print item['fqdn']
               	print item['mgmt_ip']
                print deviceinfo['description']

 	with open(filename, "wb") as csv_file:
        	csv_writer = csv.writer(
        	    csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	csv_writer.writerows(rows)
    vartotal = data['total_num_pages'];
    varItr+=1
    print varItr
    filterObj['data']['page']  = varItr
    if(varItr> vartotal):
   	 break;
