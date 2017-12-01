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
			rating = self.rdb.get_rating(restaurant_id)
			output.update({'rating': rating, 'restaurant_id': restaurant_id})
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT(self, restaurant_id):
		#set up output
		output = {'result': 'success'}
		#make id an int
		print("hello")
		restaurant_id = int(restaurant_id)
		#get data from body
		print("hi")
		data = cherrypy.request.body.read().decode()
		print("bye")
		try:
			print(data)
			data= json.loads(data)
			print("uid ", data['uid'])
			print ("rating ", data['rating'])
			self.rdb.ratings[restaurant_id][int(data['uid'])] =  data['rating']
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
