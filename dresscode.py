import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class DresscodeController(object):
	def __init__(self, rdb= None):
		self.rdb = rdb

	def GET(self):
		output = {'result': 'success'}
		try: 
			output['dresscode'] = self.rdb.get_dresscode(); 
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex) 
		return json.dumps(output) 
