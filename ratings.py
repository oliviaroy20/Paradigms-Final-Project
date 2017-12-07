import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class RatingsController(object):
	# get access to the same database all of server is using
	def __init__(self, rdb= None):
		self.rdb = rdb
	def GET_ID(self, restaurant_id):
		#set up output
		output= {'result': 'success'}
		#make the id an int
		restaurant_id = int(restaurant_id)
		#try to find in database
		try: 
			print("before rating ") 	
			rating = self.rdb.get_rating(restaurant_id)
			print("RATING: " , rating)
			output.update({'rating': rating, 'restaurant_id': restaurant_id})
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = 'get error'
		return json.dumps(output)

	def PUT(self, restaurant_id):
		#set up output
		output = {'result': 'success'}
		#make id an int
		restaurant_id = int(restaurant_id)
		#get data from body
	
		data = cherrypy.request.body.read().decode()
		try:

			data= json.loads(data)
			self.rdb.ratings[restaurant_id][data['uid']] = data['rating']
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
