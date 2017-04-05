
import xlrd
import requests
import json
import csv


class InputStruct:
  SecZone = None
  Site = None
  UnLocCode = None


rows = []
output_dir = "."
filename = "updatedtagging1_report.csv"
data =[{'id': '%s',
     "attributes":{
          "Security-Zone":"%s",
           "Site":"","UN-Location-Code":"%s"
      }
  }
]

#data2={}
data = json.dumps(data)
url = 'http://ma-gncstd-lapp08.corp.apple.com:8080/api/v1/networks/'
#baseurl= 'https://groot-api-ut.corp.apple.com/'#uat
#baseurl = 'https://groot-api-ut.corp.apple.com/'#prod
headers1 = {'content-type': 'application/json'}
def do_process():
    fname = "/Users/raja/Desktop/sample16.xlsx"
    xl_workbook = xlrd.open_workbook(fname)
    # List sheet names, and pull a sheet by name
    sheet_names = xl_workbook.sheet_names()
    xl_sheet = xl_workbook.sheet_by_index(0)
    #print ('Sheet name: %s' % xl_sheet.name)
    row = xl_sheet.row(0)  # 1st row
    from xlrd.sheet import ctype_text

    headers = []
    #print '(Column #) type:value'
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        headers.append(cell_obj.value)
    #print headers
    inputstructDict={}
    structKey=""
    for row_idx in range(1, xl_sheet.nrows): # Iterate through rows
        #print ('Row: %s' % row_idx) # Print row number
        #Condition 1
        data2 = {}
   #structKey=''
        structValue =  InputStruct()
        structValue.SecZone=[]
        structValue.Site=[]
        structValue.SecZone=[]
        structValue.UnLocCode=[]

        #   data2["attributes"]={}
        cell_obj = xl_sheet.cell(row_idx, 0) # Get cell object by row, col
        #print cell_obj
        ips = cell_obj.value.split("/");
        #print cell_obj
        data2['id']=cell_obj.value
        structKey=cell_obj.value
        #print structKey
        if inputstructDict.has_key(structKey):
            structValue = inputstructDict[structKey]
            #print structValue

        #print ips
        if (ips[1]=="30" or ips[1]=="31"):
            if "Routing" not in structValue.SecZone:
                structValue.SecZone=["Routing"]
        # Call api with routing
        #Condition 2
        cell_obj = xl_sheet.cell(row_idx,12)
        if(cell_obj.value == "OK"):
            cell_obj2 = xl_sheet.cell(row_idx,3)
            if cell_obj2.value not in structValue.Site:
                structValue.Site.append(cell_obj2.value)
        #Call the api with cell_obj2.value
        #Condition 3
        cell_obj = xl_sheet.cell(row_idx,4)
        if(len(cell_obj.value)>0):
            cell_obj2 = xl_sheet.cell(row_idx,2);
            if cell_obj2.value not in structValue.UnLocCode:
                structValue.UnLocCode.append(cell_obj2.value)
        data2={}
        data2["attributes"]={}
        data2['id']=structKey
        data2['attributes']['Security-Zone']=structValue.SecZone
        data2['attributes']['Site']=structValue.Site
        data2['attributes']['UN-Location-Code']=structValue.UnLocCode
        inputstructDict[structKey]=structValue

    data2=[]
    for k,v in inputstructDict.items():
        print k
        print v
        dataloc={}
        dataloc['id']=k
        dataloc["attributes"]={}
        dataloc['attributes']['Security-Zone']=v.SecZone
        dataloc['attributes']['Site']=v.Site
        dataloc['attributes']['UN-Location-Code']=v.UnLocCode
        data2.append(dataloc)

    data2 = json.dumps(data2)
            #print data2
    r = requests.put(url, data=data2, headers=headers1)
        #print r

    if r.status_code != 201:
       print('Status:', r.status_code, 'Problem with the request. Exiting.')
            #print data2
       rows.append(['Problem with the request. Exiting #{}'.format(data2)])
            #exit()
    else:
        # Report success
        print('Successfully added attributes #{}'.format(data2))
        rows.append(['Successfully added attributes #{}'.format(data2)])
        with open(filename, "wb") as csv_file:
           csv_writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
           csv_writer.writerows(rows)



if __name__ == "__main__":
    do_process()
