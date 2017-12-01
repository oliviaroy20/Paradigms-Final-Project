import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class ResetController(object):
	#get instance of restaurant database the server is using 
	def __init__(self, rdb = None):
		self.rdb = rdb

	def PUT(self):
		#set output 
		output = {'result': 'success'}
		
		#try to reset the data
		try:
			self.rdb.load_restaurants()
			self.rdb.load_users()
			self.rdb.load_ratings()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
		

	def PUT_ID(self, restaurant_id):
		#set up output
		output = {'result': 'success'}
		#make sure id is an int
		key = int(restaurant_id)
		#try and reset that specific restaurant
		try:
			rdb_temp = _restaurant_database()
			rdb_temp.load_restaurants()
			restaurant = rdb_temp.get_restaurant(key)
			self.rdb.set_movie(key, restaurant)

		except Exception as ex:
			output['result'] = 'error'
			outpu['message'] = str(ex)

		return json.dumps(output)
