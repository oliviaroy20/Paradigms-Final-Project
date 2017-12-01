import unittest
import requests
import json

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

if __name__ == '__main__':
	unittest.main()
