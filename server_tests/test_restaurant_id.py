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
		

	def test_movies_put(self):
		self.reset_data()
		restaurant_id = 132825
		req = requests.get(self.RESTAURANTS_URL + str(restaurant_id)
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp= json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['result'],'success')
		self.assertEqual(resp['Name'], 'puesto de tacos')
		
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
		req = requests.put(self.RESTAURANTS_URL + str(restaurant_id), data = json.dumps(m))
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['result'] , 'success')

		req = requests.get(self.RESTAURANTS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(req.content.decode('utf-8'))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['Name'], r['Name'])
		self.assertEqual(resp['Location']['Longitude'], r['Location']['Longitude'])

	

if __name__ =[ "__main__":
	unittest.main() 
