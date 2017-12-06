import cherrypy
import re, json 
from _restaurant_database import _restaurant_database

class CuisineController(object): 
	def __init__(self, rdb = None):
		self.rdb = rdb
	
	def GET(self): 
		# define output
		output = {'result': 'success'}
		try: 
			output['cuisines'] = self.rdb.get_cuisines(); 
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output) 
			
