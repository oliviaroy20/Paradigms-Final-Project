class _restaurant_database: 
	def __init__(self): 
		self.users = dict()
		self.restaurants = dict()
	
	def load_users(self): 
		self.users.clear()
		myfile = open("data/userProfile.csv")
		for line in myfile: 
			lineSplit = line.split(",")
			index = 0
			for s in lineSplit: 
				if s == "?": 
					lineSplit[index] = None
				index = index +1
			self.users[str(lineSplit[0])] = {"Smoker": lineSplit[3], "Drink Level" : lineSplit[4], "Ambience" : lineSplit[5], "Transport" : lineSplit[7], "Budget": lineSplit[17], "Cuisine": None, "Payment": None}
		myfile.close()
		myfile = open("data/userCuisine.csv")
		users = self.get_users()
		cuisine = "" 
		user = ""
		for line in myfile: 
			lineSplit = line.split(",")
			if lineSplit[0] in users: 
				if lineSplit[0] == user: 
					cuisine = cuisine + "|" + lineSplit[1].rstrip()
				else:
					user = lineSplit[0]
					cuisine = lineSplit[1].rstrip()
				self.users[str(user)]["Cuisine"] = cuisine
				
	
		myfile.close()
		myfile = open("data/userPayment.csv")
		user = ""
		payment= ""
		for line in myfile: 
			lineSplit = line.split(",")
			if lineSplit[0] in users: 
				if lineSplit[0] == user: 
					payment = payment + "|" + lineSplit[1].rstrip()
				else: 
					user = lineSplit[0]
					payment = lineSplit[1].rstrip()
				self.users[str(user)]["Payment"] = payment
		myfile.close()
					


#returns a list of user ids
	def get_users(self):
		return self.users.keys()	
			
#returns a list of a specfic user
	def get_user(self, uid): 
		uid = str(uid)
		if uid in self.get_users():	
			userList = [ self.users[uid]["Smoker"], self.users[uid]["Drink Level"], self.users[uid]["Ambience"], self.users[uid]["Transport"], self.users[uid]["Budget"], self.users[uid]["Cuisine"], self.users[uid]["Payment"]]
			return userList
		else: 
			return None 	

#add a user to the dictionary
	def set_user(self, uid, user):
		uid = str(uid)
		if uid in self.get_users(): 
			self.users[uid]["Smoker"] = user[0]
			self.users[uid]["Drink Level"] = user[1]
			self.users[uid]["Ambience"] = user[2]
			self.users[uid]["Transport"] = user[3]
			self.users[uid]["Budget"] = user[4]
			self.users[uid]["Cuisine"] = user[5]
			self.users[uid]["Payment"] = user[6]
		else: 
			userDict ={"Smoker": user[0], "Drink Level" : user[1], "Ambience": user[2], "Transport": user[3], "Budget": user[4], "Cuisine" : user[5], "Payment": user[6]}
			self.users[str(uid)] = userDict

#delete a specific user
	def delete_user(self, uid):
		if str(uid) in self.get_users():
			del self.users[str(uid)]

#read data from different data sources and create dictionaries for each restaurant 
	def load_restaurants(self): 
		self.restaurants.clear()
		#start with restaurants.csv as base of information
		myfile = open("data/restaurants.csv")
		first_line = myfile.readline()
		for line in myfile: 
			lineSplit = line.split(",")
			#change all ?s to None
			index = 0
			for s in lineSplit:
				if s == "?":
					lineSplit[index] = None
				index = index +1
			location = {"Latitude": lineSplit[1], "Longitude": lineSplit[2], "Address": lineSplit[5], "City": lineSplit[6], "State": lineSplit[7], "Country": lineSplit[8], "Zipcode": lineSplit[10] }
			self.restaurants[str(lineSplit[0])] = {"Location": location,  "Name": lineSplit[4],"Alcohol": lineSplit[11], "Smoking Area": lineSplit[12], "Dress Code": lineSplit[13], "Price": lineSplit[15], "URL": lineSplit[16]}
		myfile.close()
		myfile = open("data/restaurantPaymentAccepted.csv")
		firstLine = myfile.readline()
		payment = ""
		restaurant = ""
		restaurants = self.get_restaurants()
		for line in myfile: 
			lineSplit = line.split(",")
			if lineSplit[0] in restaurants: 	
				if lineSplit[0] == restaurant: 
					payment = payment + "|" + lineSplit[1].rstrip()
				else:
					restaurant = lineSplit[0]
					payment = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Payment Accepted"] = payment 
		myfile.close()
		myfile = open("data/restaurantCuisine.csv")
		firstLine = myfile.readline()
		restaurant = ""
		cuisine = ""
		for line in myfile:
			lineSplit = line.split(",")
			if lineSplit[0] in restaurants:
				if lineSplit[0] == restaurant:	
					cuisine = cuisine + "|" + lineSplit[1].rstrip()
				else: 
					restaurant = lineSplit[0]
					cuisine = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Cuisine"] = cuisine
		myfile.close()
		myfile = open("data/restaurantParking.csv")
		firstLine =  myfile.readline()
		restaurant = ""
		parking = ""
		for line in myfile: 
			lineSplit = line.split(",")
			if lineSplit[0] in restaurants:
				if lineSplit[0] == restaurant: 
					parking = parking +"|"+ lineSplit[1].rstrip()
				else: 	
					restaurant = lineSplit[0]
					parking = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Parking"] = parking
		myfile.close()
		myfile = open("data/restaurantHours.csv")
		firstLine =  myfile.readline()
		#if multiple entries, use the last entry in the file
		#if multiple times in an entyr, use first time given 
		for line in myfile: 
			lineSplit = line.split(",")
			if lineSplit[0] in restaurants:
				time = lineSplit[1]
				if ";" in time: 
					time = lineSplit[1].split(";")[0]
				self.restaurants[lineSplit[0]][lineSplit[2].rstrip()] = time
		myfile.close()

	def get_restaurants(self):
		return self.restaurants.keys()
				
					


