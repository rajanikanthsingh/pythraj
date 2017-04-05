import json
import requests
import xlrd
import csv
ip=id
data =[{'id': "17.200.27.4/30",
      "attributes":{
         "Security-Zone":["Routing"],
         #"UN-Location-Code":["HK"],
         #"Site":["USDAL2","USPAO1"],
      }
   }
]
data = json.dumps(data)
print data
# Set the request parameters
url = 'http://ma-gncstd-lapp08.corp.apple.com:8080/api/v1/networks/'
#baseurl= 'http://ma-gncstd-lapp08.corp.apple.com:8080/'
#baseurl = 'https://groot-api-ut.corp.apple.com/'
headers = {'content-type': 'application/json'}
# Do the HTTP put request
r = requests.put(url, data=data, headers=headers)
#r.raise_for_status()
#Check for HTTP codes other than 201
if r.status_code != 201:
    print('Status:', r.status_code, 'Problem with the request. Exiting.')
    exit()
# Report success
print('Successfully added attributes #{}'.format(data))


#Problem with the request. Exiting #[{"attributes": {"UN-Location-Code": ["KRSEL", "krsel"], "Security-Zone": [], "Site": []}, "id": "10.170.2.0/24"}]
#"10.0.177.252/31