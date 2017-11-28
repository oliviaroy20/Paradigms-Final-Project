import cherrypy
import re, json
from _restaurant_database import _restaurant_database
class RestaurantController(Object):
	def __init__(self, rdb):
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
			for key, value in self.rdb.restaurants.items():
				restaurant = self.GET_ID(key)
				output['restaurant'].append(json.load(restaurant))
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
		restaurant_id = str(restaurant_id)
	
		#try to get the data for restaurant and add it to the output
		try:
			restaurant = self.rdb.restaurants[restaurant_id]
			output.update(restaurant)
			output.update({'id': restaurant_id})
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
		 #change ids to numbers not strings 
			


