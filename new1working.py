##!/usr/bin/python
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
headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
sub_attribute_keys = ["Security-Zone","Business-Unit", "Site", "UN-Location-Code"]
#sub_attribute_keys = ["Security-Zone","Business-Unit", "Site", "UN-Location-Code"]
filename = "gnswandeviceinterface.csv"
csv_file = os.path.join(output_dir, filename).encode('utf-8')
filterObj = json.loads(filter)
devicefilters = json.loads(devicefilter)
vartmp = 0
varItr=1;
while True:
    url = 'https://capri.corp.apple.com/v0/query'
    baseurl = 'https://groot-api.apple.com/api/v1/network/'
    req = urllib2.Request(url, json.dumps(filterObj),)
    response = urllib2.urlopen(req)
    json_obj = response.read()
    data = json.loads(json_obj)
    for item in data['data'] :
        varsa=  item['id']
        #print varsa
        devicefilters['data']['Filters']['device_id'] = varsa
        request = urllib2.Request(url, json.dumps(devicefilters),)
        responses = urllib2.urlopen(request)
        json_obj = responses.read()
        deviceinterfacedata = json.loads(json_obj)
        for deviceinfo in deviceinterfacedata['data']:
            snmplocation= item['snmp_location']
            ipsubnet= deviceinfo['ip_subnet']
            split_tokens = snmplocation.split(":")
            rows.append([deviceinfo['ip_subnet'],item['snmp_location'],str[:5],str[:6]])
            break;

            #for str in split_tokens:
                #print str[:5]
                #print str[:6]
                #rows.append([deviceinfo['ip_subnet'],item['snmp_location'],str[:5],str[:6]])
                #break;

 	        #with open(filename, "wb") as csv_file:
        	#        csv_writer = csv.writer(
        	#                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        	#        csv_writer.writerows(rows)
            ##vartotal = data['total_num_pages'];
            ##varItr+=1
            ##print varItr
            ##filterObj['data']['page']  = varItr
            ##if(varItr> vartotal):
   	        ##break;
            #ips= ipsubnet
        for ip in ipsubnet:
            try:
                urls = baseurl + ip
                print ip
                        #Add your headers
                        #headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
                        #sub_attribute_keys = ["Security-Zone","Business-Unit", "Site", "UN-Location-Code"]
                request = urllib2.Request(urls, None, headers)
        #Getting the response
                response = urllib2.urlopen(request)
                json_obj = response.read()
                data1 = json.loads(json_obj)
                attribute= data1["attributes"]
                cols = []
                for sub_attrib_key in sub_attribute_keys:
                    sub_attrib_value = attribute.get( sub_attrib_key, [" "])
                    print sub_attrib_value
                    cols.append(",".join(sub_attrib_value),)
                    rows.append(cols)
                    break;
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

