# var1="Testing __init__ Package"
# var2="Hello to PyDev"
# var3="Hope you enjoy the features of the python development environment in eclipse."

import ConfigParser
import io
import openpyxl

from fileinput import filename
def readExcel():
    print "a"

def readConfig(filename):
    config=ConfigParser.RawConfigParser()
    config.read(filename)
    return config
