import cherrypy
from _restaurant_database import _restaurant_database
from reset import ResetController
from restaurants import RestaurantController
from users import UserController
from ratings import RatingsController  
def start_service(): 
	#the dispatcher tells what controller and what method should handle a request
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	rdb = _restaurant_database()
	rdb.load_restaurants()
	rdb.load_users()
	rdb.load_ratings()
	#instatiate all controllers 
	resetController = ResetController(rdb)
	restaurantController = RestaurantController(rdb)
	userController = UserController(rdb)
	ratingsController= RatingsController(rdb)
#tell the dispatcher to use the reset controller for /reset/ 
	#PUT reset all restaurants
	dispatcher.connect('reset_put', '/reset/',
		controller = resetController, 
		action = 'PUT', conditions = dict(method = ['PUT']))
	#PUT reset specific restaurant
	dispatcher.connect('reset_put_rid', '/reset/:restaurant_id',
		controller = resetController, 
		action = 'PUT_ID', conditions = dict(method= ['PUT']))
#tell dispatcher to user restaurant controller for /restaurant/ 
	#GET all restaurants 
	dispatcher.connect('restaurants_get', '/restaurants/',
		controller = restaurantController, 
		action = 'GET', conditions = dict(method=['GET']))
	#GET a specific restaurant
	dispatcher.connect('restaurants_get_id', '/restaurants/:restaurant_id', 
		controller = restaurantController, 
		action = 'GET_ID', conditions = dict(method= ['GET'])) 

	#POST new restaurant
	dispatcher.connect('restaurants_post', '/restaurants/',
		controller = restaurantController, 
		action = 'POST', conditions= dict(method = ['POST']))
	#PUT change restaurant
	dispatcher.connect('restaurants_put', '/restaurants/:restaurant_id',
		controller = restaurantController, 
		action = 'PUT', conditions = dict(method = ['PUT']))
	#DELETE all restaurants
	dispatcher.connect('restaurants_delete_all', '/restaurants/', 
		controller = restaurantController, 
		action = 'DELETE', conditions = dict(method=['DELETE']))
	#DELETE a specific restaurant
	dispatcher.connect('restaurants_delete_id', '/restaurants/:restaurant_id',
		controller = restaurantController, 
		action = 'DELETE_ID', conditions = dict(method=['DELETE']))	
#dispatch connecting /users/ to userController
	#GET all users 
	dispatcher.connect('users_get', '/users/', 
		controller = userController,
		action ='GET', conditions = dict(method=['GET']))
	#GET a specific user
	dispatcher.connect('users_get_id', '/users/:user_id',
		controller = userController, 
		action = 'GET_ID', conditions = dict(method=['GET']))
	#PUT change user
	dispatcher.connect('users_put', '/users/:user_id',
		controller = userController,
		action = 'PUT', conditions= dict(method = ['PUT']))
	#POST add new user
	dispatcher.connect('user_post', '/users/',
		controller = userController,
		action = 'POST', conditions = dict(method = ['POST']))
	#DELETE all users 
	dispatcher.connect('users_delete', '/users/',
		controller = userController, 
		action = 'DELETE', conditions = dict(method= ['DELETE']))
	#delete a specific user
	dispatcher.connect('user_delete_id', '/users/:user_id',
		controller = userController, 
		action = 'DELETE_ID', conditions = dict(method = ['DELETE']))
#dispatcher connect to /ratings/ to ratingsController 
	#GET the ratings for a specific restaurant 
	dispatcher.connect('ratings_get_id', '/ratings/:restaurant_id', 
		controller = ratingsController, 
		action = 'GET_ID', conditions = dict(method= ['GET'])) 

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

if __name__ == '__main__':
	start_service()
