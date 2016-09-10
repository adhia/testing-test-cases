'''
Created on 10-Sep-2016

@author: Adhithya
'''
from test import *
read = readConfig("config.properties")         # Common function to read a property
a = read.get("Section","test")
print(a)
def loadExcel():
    readExcel()
    print("testing")
a=loadExcel()
