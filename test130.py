#!/usr/bin/python
import xlrd
import requests
import json
#UN_Location_Code="UN-Location-Code"
#security_Zone="security-Zone"
#data =[{'id': '',
#      "attributes":{
#          "Security-Zone":"",
#           "Site":"","UN-Location-Code":""
#      }
#  }
#]
#data2={}
#data = json.dumps(data)
#url = 'http://ma-gncstd-lapp08.corp.apple.com:8080/api/v1/networks/'
#headers = {'content-type': 'application/json'}
# Do the HTTP put request
#r = requests.put(url, data=data, headers=headers)

def do_process():
    fname = "/Users/raja/Desktop/sample.xlsx"
    xl_workbook = xlrd.open_workbook(fname)
    # List sheet names, and pull a sheet by name
    sheet_names = xl_workbook.sheet_names()
    #print "SDFDS"
    #print 'Sheet Names', sheet_names, xl_workbook
    xl_sheet = xl_workbook.sheet_by_index(0)
    #print ('Sheet name: %s' % xl_sheet.name)
    row = xl_sheet.row(0)  # 1st row
    from xlrd.sheet import ctype_text

    headers = []
    #print '(Column #) type:value'
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        headers.append(cell_obj.value)

    print headers

    for row_idx in range(1, xl_sheet.nrows): # Iterate through rows
        print ('Row: %s' % row_idx) # Print row number
        #Condition 1
        #data2 = {}
        #data2["attributes"]=""

        cell_obj = xl_sheet.cell(row_idx, 0) # Get cell object by row, col
        ips = cell_obj.value.split("/");
        #print ips
        if (ips[1]=="30" or ips[1]=="31"):
            #data['id']=cell_obj.value
            #data['attributes']['Security-Zone']= "Routing"
            #r = requests.put(url, data=data, headers=headers)
            print ips[1]
        # Call api with routing


        #Condition 2
        cell_obj = xl_sheet.cell(row_idx,12)
        if(cell_obj.value == "OK"):
            cell_obj2 = xl_sheet.cell(row_idx,3)
            print cell_obj2.value
            #data[0].attributes.Site=cell_obj2.value
            #data['attributes']['Site']=cell_obj2.value
        #Call the api with cell_obj2.value


        #Condition 30

        cell_obj = xl_sheet.cell(row_idx,4)
        if(len(cell_obj.value)>0):
            cell_obj2 = xl_sheet.cell(row_idx,2);
            print cell_obj2.value
            #data[0].attributes.UN-Location-Code=cell_obj2.value
            #data['attributes']['UN-Location-Code']=cell_obj2.value
        #Call the api with cell_obj2.value
        #data2 = json.dumps(data2)
        #r = requests.put(url, data=data, headers=headers)

if __name__ == "__main__":
    do_process()