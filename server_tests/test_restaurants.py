import unittest
import requests
import json

class TestRestaurants(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RESTAURANTS_URL = SITE_URL + '/restaurants/'
	RESET_URL = SITE_URL + '/reset/'
	#reset the data for each test for easy testing 
	def reset_data(self):
		r = {}
		request = requests.put(self.RESET_URL, data = json.dumps(r))
	#check if the response is in JSON format 
	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False 
	def test_movies_get_all(self):	
		self.reset_data()
		r = requests.get(self.RESTAURANTS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		#restaurants value of a dictionary with key "restaurants"
		restaurants = resp['restaurants']
		for restaurant in restaurants:
			if restaurant['id'] == 132825:
				testrestaurant = restaurant
		self.assertEqual(testrestaurant['Location']['Latitude'], '22.1473922')
		self.assertEqual(testrestaurant['Name'], 'puesto de tacos')
		self.assertEqual(testrestaurant['Location']['Zipcode'], '78280')


if __name__ == "__main__":
	unittest.main()
