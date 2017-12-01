import cherrypy
import re, json
from _restaurant_database import _restaurant_database

class RecController(object):
	def __init__(self, rdb=None):
		self.rdb = rdb

	def GET(self):
		output = {'result': 'success'}

		try:
		########PROBABLY FIX PARAMETERSSSS###########
			output['recommendations'] = self.rdb.filter_restaurants()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self):
		output = {'result': 'success'}
		data = cherrypy.request.body.read().decode()
		try:
			data = json.loads(data)
			self.rdb.set_filters(data["Cuisine"], data["Dress Code"], data["Payment Accepted"], data["Price"])
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

