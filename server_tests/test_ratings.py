import unittest
import requests
import json

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

if __name__ == '__main__':
	unittest.main()
