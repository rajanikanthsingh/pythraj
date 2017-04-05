#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import urllib2
import urllib
import json
import csv
import sys
import re
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

filter = """
{
  "data": {
    "page": 1,
    "Type": "Device",
    "Filters": {
      "support_group__name": "GNS WAN",
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
filename = "gnswandeviceinterface.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')
filterObj = json.loads(filter)
devicefilters = json.loads(devicefilter)
vartmp = 0
varItr=1;
while True:
    url = 'https://capri.corp.apple.com/v0/query'
    url1 = 'https://groot-api.apple.com/api/v1/network/'
    req = urllib2.Request(url, json.dumps(filterObj),)
    response = urllib2.urlopen(req)
    json_obj = response.read()
    data = json.loads(json_obj)
    for item in data['data'] :
        varsa=  item['id']
        #snmplocation= item['snmp_location']
        #print snmplocation
        #if snmplocation is not None:
        #    split_tokens = snmplocation.split(':')
        #    print split_tokens
        #print snmplocation
        #location= item['snmp_location'] [:5]
        #site= item['snmp_location'] [:6]
        #print varsa
        devicefilters['data']['Filters']['device_id'] = varsa
        request = urllib2.Request(url, json.dumps(devicefilters),)
        responses = urllib2.urlopen(request)
        json_obj = responses.read()
        deviceinterfacedata = json.loads(json_obj)
        #yourstring = deviceinterfacedata.encode('ascii', 'ignore').decode('ascii')
        #deviceinterfacedata.encode('utf-8')
        #print  deviceinterfacedata
        #for deviceinfo in deviceinterfacedata['data']:
		#rows.append([deviceinfo['ip_subnet'],item['snmp_location']])
	        #print deviceinfo['name']
       		#print deviceinfo['ip']
       		#print deviceinfo['ip_subnet']
       		#print deviceinfo['id']
       		#print deviceinfo['device_name']
        	#print item['snmp_location']
               	#print item['fqdn']
               	#print item['mgmt_ip']
                #print deviceinfo['description']
                #location= item['snmp_location'] [:5]
                #site= item['snmp_location'] [:6]
                #print item['snmp_location'] [:5]
                #print item['snmp_location'] 
                #print site
                #re.split('[:]', snmplocation)

        for deviceinfo in deviceinterfacedata['data']:
              snmplocation= item['snmp_location']
              ipsubnet= deviceinfo['ip_subnet']
              # print ipsubnet
              split_tokens = snmplocation.split(":")
              for str in split_tokens:
                  print str[:5]
                  print str[:6]
                  #print deviceinfo['ip_subnet']
                  #print item['snmp_location']
                  #print str[:6]
                  rows.append([deviceinfo['ip_subnet'],item['snmp_location'],str[:5],str[:6]])
                  break;
              #print  snmplocation
                 #url1 = 'https://groot-api.apple.com/api/v1/network/'
              #for item in ipsubnet:

                #r = requests.get(
                #    url1,
                #    data=item
                #    )
                #data = r.json()
                #response_text = r.text
                #json_data = json.loads(response_text)
                #data = json_data
                #print data

        #for deviceinfo in deviceinterfacedata['data']:
              #snmplocation= item['snmp_location']
              #if snmplocation is not None:
                #split_tokens = snmplocation.split(':')
              #if len(split_tokens) > 1:
                    #temp_site = split_tokens[1]
              #if re.match('^[a-zA-Z][0-9]{}$',temp_site):
              #if re.match('^(([a-zA-Z]{2}\d{2})|([a-zA-Z]{2}\d{1}))$', temp_site) is not None or re.match('^[a-zA-Z]{1}\d{3}$',temp_site)or re.match('^[a-zA-Z]{5}\d{1}', temp_site):
                #site = temp_site
                #print site
              #print split_tokens
        #for item in split_tokens:
              #print[item] [:5]
              #if snmplocation is not None:
                #split_tokens = snmplocation.split(':')
                #print split_tokens
                #if len(split_tokens) > 1:
                #    temp_site = split_tokens[1]
                #sl=  split_tokens
                #print sl
                #if re.match('^(([a-zA-Z]{2}\d{2})|([a-zA-Z]{2}\d{1}))$', sl) is not None or re.match(
                #        '^[a-zA-Z]{1}\d{3}$',
                #        temp_site) or re.match(
                 #   '^[a-zA-Z]{5}\d{1}', sl):
                 #   site = sl
                 #   print site

        #print snmplocation
        #location= item['snmp_location'] [:5]
        #site= item['snmp_location'] [:6]
 	with open(filename, "wb") as csv_file:
        	csv_writer = csv.writer(
        	    csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	csv_writer.writerows(rows)
    vartotal = data['total_num_pages'];
    varItr+=1
    #print varItr
    filterObj['data']['page']  = varItr
    if(varItr> vartotal):
   	 break;

	

