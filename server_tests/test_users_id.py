import unittest
import requests
import json

class TestUsers(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	USERS_URL = SITE_URL + '/users/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		r = {}
		req = requests.put(self.RESET_URL, data = json.dumps(r))

	def is_json(self, resp):
		try: 	
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_users_get(self):
		self.reset_data()
		user_id = 1002
		req = requests.get(self.USERS_URL+ str(user_id))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['Smoker'], 'false')
		self.assertEqual(resp['Budget'], 'low')



if __name__ =='__main__':
	unittest.main() 
