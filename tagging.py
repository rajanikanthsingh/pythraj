#!/usr/bin/python
import os
import urllib2
import xlrd
import urllib
import json
import csv
import requests
from collections import OrderedDict


# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('/Users/raja/Desktop/sample.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
list = []

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    list1 = OrderedDict()
    row_values = sh.row_values(rownum)
    list1['ip'] = row_values[0]
    print list1

    #list1[ipsubnet] = row_values[0]
    #list1['country'] = row_values[1]
    #list1['Sitecodevalidation'] = row_values[2]
    #list1['miles'] = row_values[3]





































