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

	#create a new user
	def POST(self):
		#define output
		output = {'result': 'success'}
		#get data 
		data = cherrypy.request.body.read().decode()
		try:
			data = json.loads(data)
			maxKey =0
			for key in self.rdb.get_users():
				if int(key) > maxKey:
					maxKey = key
			self.rdb.users[int(maxKey) +1] = data
			output['id'] = int(maxKey) +1 
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output) 

	#change a user
	def PUT(self, user_id):
		#define output
		output = {'result': 'success'}
		#make sure id is an int
		user_id = int(user_id)
		#get data
		data = cherrypy.request.body.read().decode()
		try:
			data = json.loads(data)
			self.rdb.users[user_id] = data
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	#delete all users
	def DELETE(self):
		#define output
		output = {'result': 'success'}
		#try to delete all users
		try: 
			self.rdb.users = dict()
		except Exception as ex:
			output['result'] =  'error'
			outpu['message'] = str(ex)
		return json.dumps(output)		
	#delete a specifc user
	def DELETE_ID(self, user_id):
		#define output
		output = {'result': 'success'}	
		#make user id an int
		user_id = int(user_id)
		try:
			self.rdb.delete_user(user_id)
		except Exception as ex:
			output['result'] = 'error'	
			output['message'] =  str(ex)
		return json.dumps(output)





