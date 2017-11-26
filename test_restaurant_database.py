from _restaurant_database import _restaurant_database
import unittest


class TestRestaurantDatabase(unittest.TestCase): 
	"""unit tests for restaurant API"""
	
	#@classmethod
	#def setUpClass(self):
	rdb = _restaurant_database()

	def reset_data(self): 
		self.rdb.load_users()

	def test_get_user(self):
		self.reset_data()
		user = self.rdb.get_user("U1002")
		self.assertEquals(user[0],  'false')
		self.assertEquals(user[1], 'abstemious')
		self.assertEquals(user[2], 'informal')
		self.assertEquals(user[3], 'public')
		self.assertEquals(user[4], 'low')
		self.assertEquals(user[5], 'Mexican')
		self.assertEquals(user[6], 'cash')
	



if __name__ == "__main__":
	unittest.main() 
