import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class PriceController(object):
	def __init__(self, rdb= None):
		self.rdb = rdb
	
	def GET(self):
		output = {'result': 'success'} 
		try: 
			output['price'] = self.rdb.get_prices();
		except Exception as ex: 
			output['result'] = 'errror'
			output['message'] = str(ex)
		return json.dumps(output)
