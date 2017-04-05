#!/usr/bin/python
import urllib
import urllib2
import json
#import urllib.parse
#from urlparse import urlparse
import json
import requests
import urlparse
#getVars = {'17.0.142.104/31'}
#ip='17.0.142.104/31'
ip =['17.0.142.100/31', '17.0.142.104/31', '17.0.142.206/31', '17.0.142.82/31']
for ip in ip:1
    #print ip
#url = 'https://groot-api.apple.com'
    parsed = urlparse.urlparse("https://groot-api.apple.com")
#headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
#urlparse.urlparse(url)
    #getvars='/api/v1/network/%s.' % ip
    #print getvars
    #url = parsed._replace(path="%s" %getvars)
    urls =  parsed._replace(path="/api/v1/network/%s." %ip)
    print urls
    #for url in urls:
        #r = requests.get(url, { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'});
        #content = resp.content
        #data = r.json()
        #print data

    #headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}
#Create the Request.
    #request = urllib2.Request(url, None, headers)
    #response = urllib2.urlopen(request)
    #json_obj = response.read()
    #data1 = json.loads(json_obj)
    #print data1

#r = requests.get('url')
#data = r.json()
#print data
#attribute= data1["attributes"]
#print attribute["Security-Zone"]
#params = {"ipsubnet" : "17.0.142.104/31" }
#r=requests.get(url, data=params)
#data = r.json()
#print data
#import urllib.parse
#getVars = {'ipsubnet': '17.0.142.104/31'}
#print(url + urllib.parse.urlencode(getVars)
#print(url + urlparse(getVars))
#filter = """
#{17.0.142.104/31}"""
#url = 'https://groot-api.apple.com/api/v1/network/'
#headers = { 'GNSD-APP-ID': '181','GNSD-APP-KEY': 'subnet-tagging-raja-api-key-123'}

#response = requests.get(url=url, params=filter,)
#data = json.load(response)