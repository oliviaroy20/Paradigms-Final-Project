import unittest
import requests
import json


### INCLUDES ALL TESTS ###

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
		req = requests.get(self.RESTAURANTS_URL + str(restaurant_id))
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
		req = requests.put(self.RESTAURANTS_URL + str(restaurant_id), data = json.dumps(r))
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['result'] , 'success')

		req = requests.get(self.RESTAURANTS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['Name'], r['Name'])
		self.assertEqual(resp['Location']['Longitude'], r['Location']['Longitude'])

	def test_restaurants_delete(self):
		self.reset_data()
		restaurant_id = 132825
		r = {}
		req = requests.delete(self.RESTAURANTS_URL + str(restaurant_id), data = json.dumps(r))
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')
		
		req = requests.get(self.RESTAURANTS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(req.content.decode('utf-8')))
		resp = json.loads(req.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')
		self.assertEqual(resp['message'], str(restaurant_id))



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
		req = requests.get(self.USERS_URL)
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		
		testuser= {}
		testuser['Smoker'] = 'true'
		testuser['Budget'] = 'high'
		
		users = resp['users']
		for user in users:
			if user['id'] == 1002:
				testuser = user
		self.assertEqual(testuser['Smoker'], 'false')
		self.assertEqual(testuser['Budget'], 'low')

	def test_users_post(self):
		self.reset_data()
		u = {}
		u['Smoker'] = 'false'
		u['Drink Level']= 'social drinker'
		u['Ambience'] = 'informal'
		u['Transport'] = 'public'
		u['Budget'] = 'low'
		u['Cuisine'] = 'American'
		u['Payment'] = 'cash' 
		req = requests.post(self.USERS_URL, data = json.dumps(u))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['id'], 1139)
		
		req= requests.get(self.USERS_URL + str(resp['id']))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['Smoker'], u['Smoker'])
		self.assertEqual(resp['Cuisine'], u['Cuisine'])

	def test_users_delete(self):
		self.reset_data()
		u = {}
		req = requests.delete(self.USERS_URL, data = json.dumps(u))
		self.assertTrue(self.is_json(req.content.decode()))
		resp= json.loads(req.content.decode())
		self.assertEqual(resp['result'] ,'success')
		
		req = requests.get(self.USERS_URL)
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		users = resp['users']
		self.assertFalse(users)


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

	def test_users_put(self):
		self.reset_data()
		user_id = 1002
		req =requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['Smoker'], 'false')
		self.assertEqual(resp['Budget'], 'low')
		u = {}
		u['Smoker'] = 'false'
		u['Drink Level']= 'social drinker'
		u['Ambience'] = 'informal'
		u['Transport'] = 'public'
		u['Budget'] = 'low'
		u['Cuisine'] = 'American'
		u['Payment'] = 'cash'

		req = requests.put(self.USERS_URL + str(user_id), data = json.dumps(u))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['result'], 'success')

		req = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['Smoker'], u['Smoker'])
		self.assertEqual(resp['Cuisine'] , u['Cuisine'])


	def test_users_delete(self):
		self.reset_data()
		user_id =1002 
		u = {}
		req = requests.delete(self.USERS_URL + str(user_id), data = json.dumps(u))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['result'], 'success')
		
		req = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(req.content.decode()))
		resp = json.loads(req.content.decode())
		self.assertEqual(resp['result'], 'error') 
		self.assertEqual(resp['message'], str(user_id))


class TestRatings(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		r = requests.put(self.RESET_URL)
	def is_json(self, resp):
		try: 
			json.loads(resp)
			return True
		except ValueError: 
			return False
	def test_rating_get(self):
		self.reset_data()
		restaurant_id =132825
		r = requests.get(self.RATINGS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['rating'], [1.28125, 1.34375, 0.9375])
		self.assertEqual(resp['restaurant_id'] , restaurant_id)

	def test_rating_put(self):
		self.reset_data()
		restaurant_id = 132825
		rating = {'uid': 1002, 'rating': [1, 1,1]}
		r = requests.put(self.RATINGS_URL + str(restaurant_id), data = json.dumps(rating))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertTrue(resp['result'], 'success')
		
		r = requests.get(self.RATINGS_URL + str(restaurant_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertTrue(resp['rating'], 1.25)


class TestRecommendations(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RECS_URL = SITE_URL + '/recommendations/'
	RESET_URL = SITE_URL + '/reset/'

	#reset the data for each test for easy testing
	def reset_data(self):
		r = []
		request = requests.put(self.RESET_URL, data = json.dumps(r))

	#check if the response is in JSON format
	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_recommendations_get(self):
		self.reset_data()
		r = requests.get(self.RECS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		self.assertEqual(resp['recommendations']['134999']['Price'], 'medium')


	def test_recommendations_post(self):
		self.reset_data()
		r = {}
		r['Cuisine'] = 'Mexican'
		r['Price'] = 'low'
		r['Dress Code'] = 'casual'
		r['Payment Accepted'] = 'cash'

		req = requests.post(self.RECS_URL, data=json.dumps(r))

		self.assertTrue(self.is_json(req.content.decode()))
		response = json.loads(req.content.decode())
		self.assertEqual(response['result'], 'success')

class TestRest(unittest.TestCase):
	PORT_NUM = '51067'
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	RESET_URL = SITE_URL + '/reset/'

	def test_reset_data(self):
		r = {}
		resp = requests.put(self.RESET_URL)

if __name__ =="__main__":
	unittest.main() 
