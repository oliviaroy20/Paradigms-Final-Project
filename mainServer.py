import cherrypy
from _restaurant_database import _restaurant_database

def start_service(): 
	#the dispatcher tells what controller and what method should handle a request
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	rdb = _restaurant_database()
	rdb.load_restaurants()
	rdb.load_users()
	rdb.load_ratings()
	
	#configure the server to user student04 and port 51067
	#configure server so the dispatcher is the one defined at top of method
	conf = {'global': {
		'server.socket_host': 'student04.cse.nd.edu', 
		'server.socket_port': 51067
		},
		'/': {'request.dispatch': dispatcher}
		}
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config= conf)
	cherrypy.quickstart(app)

if __name__ = '__main__':
	start_service()
