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
	def test_restaurant_get_all(self):	
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


	def test_restaurant_post(self):
		self.reset_data()
		r = {}
		r['Location'] = {}
		r['Location']['Latitude'] = '123'
		r['Location']['Longitude'] = '456'
		r['Location']['Address'] ='main street'
		r['Location']['City'] = 'south bend'
		r['Location']['State'] = 'indiana'
		r['Location']['Zipcode']= '00000'
		r['Name'] = 'restaurant'
		r['Alcohol'] = 'Wine-Beer'
		r['Smoking Area'] = 'none'
		r['Dress Code'] = 'informal'
		r['Price'] = 'low'
		r['URL'] = 'restaurant.com'
		r['Sun;'] = '12:00 - 20:00'
		r['Sat;'] = '12:00 - 20:00'
		r['Mon;Tue;Wed;Thu;Fri;'] = '12:00 - 20:00'
		r['Payment Accepted'] = 'cash'
		r['Cuisine'] = 'Mexican'
		r['Parking'] = 'valet' 
		req = requests.post(self.RESTAURANTS_URL, data = json.dumps(r))
		self.assertTrue(self.is_json(req.content.decode()))
		response = json.loads(req.content.decode())
		self.assertEqual(response['result'], 'success')
		self.assertEqual(response['id'], 135110)
	
		req = requests.get(self.RESTAURANTS_URL + str(response['id']))
		self.assertTrue(self.is_json(req.content.decode()))
		response = json.loads(req.content.decode())
		self.assertEqual(response['Name'] , r['Name'])
		self.assertEqual(response['Cuisine'], r['Cuisine'])
		self.assertEqual(response['Location']['Longitude'], r['Location']['Longitude'])
	
	def test_restauratant_delete(self):
		self.reset_data()
		r = {}
		req = requests.delete(self.RESTAURANTS_URL, data = json.dumps(r))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['result'], 'success')
		
		req = requests.get(self.RESTAURANTS_URL)
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		restaurants = resp['restaurants']
		self.assertFalse(restaurants)











if __name__ == "__main__":
	unittest.main()
