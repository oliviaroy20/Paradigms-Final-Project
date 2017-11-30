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
		user = self.rdb.get_user(1002)
		self.assertEquals(user[0],  'false')
		self.assertEquals(user[1], 'abstemious')
		self.assertEquals(user[2], 'informal')
		self.assertEquals(user[3], 'public')
		self.assertEquals(user[4], 'low')
		self.assertEquals(user[5], 'Mexican')
		self.assertEquals(user[6], 'cash')

	def test_set_user(self):
		self.reset_data()
		user = self.rdb.get_user(1002)
		user[3] = 'car owner' 
		user[4]= 'high'
		self.rdb.set_user(1002, user)
		user = self.rdb.get_user("1002")
		self.assertEquals(user[0], 'false')
		self.assertEquals(user[1], 'abstemious')
		self.assertEquals(user[2], 'informal')
		self.assertEquals(user[3], 'car owner')
		self.assertEquals(user[4], 'high')
		self.assertEquals(user[5], 'Mexican')
		self.assertEquals(user[6], 'cash')

	def test_delete_user(self):
		self.reset_data()
		self.rdb.delete_user("1002")
		user = self.rdb.get_user("1002")
		self.assertEquals(user, None)
	

	def test_get_restaurant(self): 
#		for key,values in self.rdb.restaurants.items():
#			print(self.rdb.get_restaurant(key))	
		self.reset_data()
		r =self.rdb.get_restaurant(132825)
		self.assertEquals(r[0][0], '22.1473922')
		self.assertEquals(r[1], 'puesto de tacos')
		self.assertEquals(r[2], 'No_Alcohol_Served')
		self.assertEquals(r[3], 'none')
		self.assertEquals(r[4], 'informal')
		self.assertEquals(r[5], 'low')
		self.assertEquals(r[6], None) 
		
	def test_set_restaurant(self):
		self.reset_data()
		r = self.rdb.get_restaurant(132825)
		r[0][0] = "150"
		r[1] = "new name"
		r[5] = "high"
		r[6] = "url"
		self.rdb.set_restaurant(132825, r)
		r = self.rdb.get_restaurant(132825)
		self.assertEquals(r[0][0] , "150")
		self.assertEquals(r[1]	, "new name")
		self.assertEquals(r[2], "No_Alcohol_Served")
		self.assertEquals(r[3], "none")
		self.assertEquals(r[4], "informal")
		self.assertEquals(r[5], "high")
		self.assertEquals(r[6], "url")

	def test_delete_restaurant(self):
		self.reset_data()
		self.rdb.delete_restaurant(132825)
		r = self.rdb.get_restaurant(132825)
		self.assertEquals(r, None)

	def test_get_rating(self):
		self.reset_data()
		rating = self.rdb.get_rating("132825")
		self.assertEquals(rating, 1.28125)

	def test_get_foodrating(self):
		self.reset_data()
		rating = self.rdb.get_foodrating("132825")
		self.assertEquals(rating, 1.34375)

	def test_get_servrating(self):
		self.reset_data()
		rating = self.rdb.get_servrating("132825")
		self.assertEquals(rating, 0.9375)

	def test_set_user_restaurant_ratings_change(self):
		#test for changing existing user rating
		self.reset_data()
		#print(self.rdb.get_rating("132825"))
		self.rdb.set_user_restaurant_ratings(1002, 132825, [1, 1, 1])
		newRating = self.rdb.get_rating(132825)
		#print(newRating)
		self.assertEquals(newRating, 1.25)

	def test_set_user_restaurant_ratings_add(self):
		#test for adding ratings for an existing user
		self.reset_data()
		self.rdb.set_user_restaurant_ratings(1096, "132825", [1, 1, 1])
		newRating = self.rdb.get_rating("132825")
		self.assertEquals(newRating, 1.2727272727272727)
	

	def test_filter_by_price(self):
		self.reset_data()
		matches = self.rdb.filter_by_price("high")
		self.assertEquals(matches, [135040, 132875, 135065,
		135076, 132862, 134983, 135045, 135054, 134975,
		135053, 135050, 135079, 134992, 135080, 135066,
		135055, 135074, 135064, 135052, 135026, 135047,
		135035, 135048, 135073, 134986])

	def test_filter_by_cuisine(self):
		self.reset_data()
		matches = self.rdb.filter_by_cuisine("Mexican")
		self.assertEquals(len(matches), 28)

	def test_filter_by_dresscode(self):
		self.reset_data()
		matches = self.rdb.filter_by_dresscode("casual")
		self.assertEquals(len(matches), 10)

	def test_filter_by_payment(self):
		self.reset_data()
		matches = self.rdb.filter_by_payment("cash")
		self.assertEquals(len(matches), 113)

if __name__ == "__main__":
	unittest.main() 
