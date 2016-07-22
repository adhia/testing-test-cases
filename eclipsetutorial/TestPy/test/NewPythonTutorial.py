from __init__ import *
print(var1)
print(var2)
print(var3)
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        pass

if __name__ == '__main__':
    unittest.main()