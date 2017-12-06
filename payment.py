import cherrypy 
import re, json
from  _restaurant_database import _restaurant_database

class PaymentController(object):
	def __init__(self, rdb = None):
		self.rdb = rdb

	def GET(self):
		output = {'result': 'success'}
		try: 
			output['payment'] =  self.rdb.get_payments()
		except Exception as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
