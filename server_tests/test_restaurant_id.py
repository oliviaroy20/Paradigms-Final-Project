import unittest
import requests
import json

class TestRestaurantsId(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RESTAURANTS_URL = SITE_URL + '/restaurants/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		restaurants = {}
		r = requests.put(self.RESET_URL, data = json.dumps(restaurants))
	#test if respons is in JSON format
	def is_json(self, resp):
		try: 
			json.loads(resp)
			return True
		except ValueError: 
			return False

	def test_movies_get(self): 	
		self.reset_data()
		restaurant_id = 132825
		r = requests.get(self.RESTAURANTS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['Location']['Latitude'], '22.1473922')
		self.assertEqual(resp['Name'] , 'puesto de tacos')
		self.assertEqual(resp['Dress Code'], 'informal')
		

if __name__ == "__main__":
	unittest.main() 
