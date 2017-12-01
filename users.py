import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class UserController(object):
	#get the same instance of the database the whole server is using 
	def __init__(self, rdb): 
		self.rdb = rdb
	def GET(self):
		#define output
		output = {'result': 'success'}
		try: 
			output['users'] = []
			for key, value in self.rdb.users.items():
				user = self.GET_ID(key)
				output['users'].append(json.loads(user))
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	#get a specific user
	def GET_ID(self, user_id):
		#define output
		output = {'result' :'success'}
		#make sure id is an int
		user_id = int (user_id)
		#try to get userif it exists
		try:	
			user = self.rdb.users[user_id]
			output.update(user)
			output.update({'id': user_id})
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
