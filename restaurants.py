import cherrypy
import re, json
from _restaurant_database import _restaurant_database
class RestaurantController(object):
	def __init__(self, rdb = None):
		#have own instance of the restaurant database API so that it can access the current information 
		self.rdb = rdb
	
	#GET for /restaurants, returns a dictionary of an array of restaurants
	def GET(self):
		#define output
		output = {'result': 'success'}
		#try to get the data
		try:
			output['restaurants'] = []
			#for each restaurant in the database,use the get by id to get information about every restaurant 
		
			for key in self.rdb.get_restaurants():
				output['restaurants'].append(json.loads(self.GET_ID(key)))
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		#return the output: either error (hopefully not) or the restaurants
		return json.dumps(output)

	#get a dictionary of the specified restaurant 
	def GET_ID(self, restaurant_id):
		#define output
		output = {'result': 'success'}
		#make sure id is a string
		restaurant_id = int(restaurant_id)
		print (restaurant_id)
		#try to get the data for restaurant and add it to the output
		try:
			restaurant = self.rdb.restaurants[restaurant_id]
			print("Restaurant " , restaurant)
			output.update(restaurant)
			output.update({'id': restaurant_id})
			print ("output ", output)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		#return output dictionary as json
		return json.dumps(output)
			 
	#add a restaurant to the datasource 
	def POST(self):
		#define output
		output = {'result': 'success'}
		#get the input and put in correct format
		data = cherrypy.request.body.read().decode()
		try: 
			data = json.loads(data)
			#find the maximum key to create next key for new restaurant 
			maxKey =0
			for key in self.rdb.get_restaurants():
				if (int(key)>maxKey):
					maxKey = key
			self.rdb.restaurants[int(maxKey)+1] = data
			output['id'] = int(maxKey) +1
		except Exception as ex: 
			output['result'] = 'error' 
			output['message'] = str(ex)
		return json.dumps(output) 
			
	#change a restauranct given an id
	def PUT(self, restaurant_id):
		#set up output
		output = {'result': 'success'}
		#make sure id is an int
		restaurant_id = int(restaurant_id)
		#get data
		data = cherrypy.request.body.read().decode()
		try: 
			data = json.loads(data)	
			self.rdb.restaurants[restaurant_id] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	#delete all restaurants
	def DELETE(self):
		#define output
		output = {'result' :'success'}
		#clear all restaurants
		try: 
			self.rdb.restaurants = dict()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	#delete a specific restaurant
	def DELETE_ID(self, restaurant_id):
		output = {'result' : 'success'}
		restaurant_id = int(restaurant_id)
		try: 
			self.rdb.delete_restaurant(restaurant_id)
		except Exception as ex: 
			output['result'] = 'error' 
			output['message'] = 'restaurant not found'
		return json.dumps(output)
		



