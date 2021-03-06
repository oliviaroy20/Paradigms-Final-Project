import cherrypy
from _restaurant_database import _restaurant_database
from reset import ResetController
from restaurants import RestaurantController
from users import UserController
from ratings import RatingsController 
from recommendations import RecController
from options import OptionsController
from cuisine import CuisineController
from dresscode import DresscodeController
from payment import PaymentController
from price import PriceController 
def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"
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
	recController = RecController(rdb)
	optionsController = OptionsController()
	cuisineController = CuisineController(rdb)
	dresscodeController = DresscodeController(rdb)
	paymentController = PaymentController(rdb)
	priceController = PriceController(rdb) 
#connect options for each resource 
	dispatcher.connect('options_reset', '/reset/', 
		controller = optionsController, 
		action = 'OPTIONS', conditions= dict(method = ['OPTIONS']))
	dispatcher.connect('options_reset_restaurant', '/reset/:restaurant_id',
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method =['OPTIONS']))
	dispatcher.connect('options_restaurants', '/restaurants/',
		controller = optionsController,
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_rid', '/restaurants/:restaurant_id',
		controller = optionsController,
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_users', '/users/',
		controller = optionsController, 
		action= 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_uid', '/users/:user_id',
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_ratings', '/ratings/:restaurant_id',
		controller = optionsController,
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_recommendations', '/recommendations/',
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_cuisine', '/cuisine/',
		controller = optionsController,
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_dress', '/dresscode/',
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_payment', '/payments/', 
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
	dispatcher.connect('options_price', '/prices/',
		controller = optionsController, 
		action = 'OPTIONS', conditions = dict(method = ['OPTIONS']))
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
	#PUT new rating 
	dispatcher.connect('ratings_put', '/ratings/:restaurant_id', 
		controller = ratingsController, 
		action = 'PUT', conditions = dict(method = ['PUT']))
#dispatcher connect to /recommendations/ to recController
	#POST new filters
	dispatcher.connect('recs_post', '/recommendations/',
		controller = recController,
		action = 'POST', conditions = dict(method = ['POST']))

	#GET filtered results
	dispatcher.connect('recs_get', '/recommendations/',
		controller = recController,
		action = 'GET', conditions = dict(method = ['GET']))
#/cuisine/
	dispatcher.connect('cuisine_get', '/cuisine/', 
		controller = cuisineController, 
		action = 'GET', conditions = dict(method = ['GET']))
#/dresscode/
	dispatcher.connect('dresscode_get', '/dresscode/', 
		controller = dresscodeController,
		action = 'GET', conditions = dict(method = ['GET']))
#/payments/
	dispatcher.connect('payments_get', '/payments/',
		controller = paymentController, 
		action= 'GET', conditions = dict(method = ['GET']))
#/prices/
	dispatcher.connect('prices_get',  '/prices/',
		controller = priceController, 
		action = 'GET', conditions = dict(method = ['GET']))

	#configure the server to user student04 and port 51067
	#configure server so the dispatcher is the one defined at top of method
	conf = {'global': {
		'server.socket_host': 'student04.cse.nd.edu', 
		'server.socket_port': 51067
		},
		'/': {'request.dispatch': dispatcher, 'tools.CORS.on':True}
		}
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config= conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
