from __init__ import *
import unittest
print(var1)
print(var2)
print(var3)
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (tinydict.keys())   # Prints all the keys
class test(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print (tinydict.values()) # Prints all the values

if __name__ == '__main__':
    unittest.main()
