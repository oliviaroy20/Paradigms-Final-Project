from _restaurant_database import _restaurant_database
import unittest


class TestRestaurantDatabase(unittest.TestCase): 
	"""unit tests for restaurant API"""
	
	#@classmethod
	#def setUpClass(self):
	rdb = _restaurant_database()

	def reset_data(self): 
		self.rdb.load_users()
		self.rdb.load_restaurants()
		self.rdb.load_ratings()

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

	def test_set_user(self):
		self.reset_data()
		user = self.rdb.get_user("U1002")
		user[3] = 'car owner' 
		user[4]= 'high'
		self.rdb.set_user("U1002", user)
		user = self.rdb.get_user("U1002")
		self.assertEquals(user[0], 'false')
		self.assertEquals(user[1], 'abstemious')
		self.assertEquals(user[2], 'informal')
		self.assertEquals(user[3], 'car owner')
		self.assertEquals(user[4], 'high')
		self.assertEquals(user[5], 'Mexican')
		self.assertEquals(user[6], 'cash')

	def test_delete_user(self):
		self.reset_data()
		self.rdb.delete_user("U1002")
		user = self.rdb.get_user("U1002")
		self.assertEquals(user, None)
	

	def test_get_restaurant(self): 
#		for key,values in self.rdb.restaurants.items():
#			print(self.rdb.get_restaurant(key))	
		self.reset_data()
		r =self.rdb.get_restaurant("132825")
		self.assertEquals(r[0][0], '22.1473922')
		self.assertEquals(r[1], 'puesto de tacos')
		self.assertEquals(r[2], 'No_Alcohol_Served')
		self.assertEquals(r[3], 'none')
		self.assertEquals(r[4], 'informal')
		self.assertEquals(r[5], 'low')
		self.assertEquals(r[6], None) 
		
	def test_set_restaurant(self):
		self.reset_data()
		r = self.rdb.get_restaurant("132825")
		r[0][0] = "150"
		r[1] = "new name"
		r[5] = "high"
		r[6] = "url"
		self.rdb.set_restaurant("132825", r)
		r = self.rdb.get_restaurant("132825")
		self.assertEquals(r[0][0] , "150")
		self.assertEquals(r[1]	, "new name")
		self.assertEquals(r[2], "No_Alcohol_Served")
		self.assertEquals(r[3], "none")
		self.assertEquals(r[4], "informal")
		self.assertEquals(r[5], "high")
		self.assertEquals(r[6], "url")

	def test_delete_restaurant(self):
		self.reset_data()
		self.rdb.delete_restaurant("132825")
		r = self.rdb.get_restaurant("132825")
		self.assertEquals(r, None)

	def test_get_rating(self):
		self.reset_data()
		rating = self.rdb.get_rating("132825")
		self.assertEquals(rating, 1.28125)

if __name__ == "__main__":
	unittest.main() 
