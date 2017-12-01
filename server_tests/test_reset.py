import unittest
import requests
import json

class TestRest(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		r = {}
		resp = requests.put(self.RESET_URL)

if __name__ =="__main__":
	unittest.main() 
