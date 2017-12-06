class _restaurant_database: 
	def __init__(self): 
		self.users = dict()
		self.restaurants = dict()
		self.ratings = dict()
		self.filters = {"Price": "None", "Cuisine": "None", "Dress Code": "None", "Payment Accepted": "None"}
	
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
			self.users[int(lineSplit[0][1:])] = {"Smoker":
			lineSplit[3], "Drink Level" : lineSplit[4], "Ambience" :
			lineSplit[5], "Transport" : lineSplit[7], "Budget":
			lineSplit[17], "Cuisine": None, "Payment": None}
		myfile.close()
		myfile = open("data/userCuisine.csv")
		users = self.get_users()
		cuisine = "" 
		user = -1
		for line in myfile: 
			lineSplit = line.split(",")
			uidTemp = int(lineSplit[0][1:])
			if uidTemp in users: 
				if uidTemp == user: 
					cuisine = cuisine + "|" + lineSplit[1].rstrip()
				else:
					user = uidTemp
					cuisine = lineSplit[1].rstrip()
				self.users[user]["Cuisine"] = cuisine
				
	
		myfile.close()
		myfile = open("data/userPayment.csv")
		user = -1
		payment= ""
		for line in myfile: 
			lineSplit = line.split(",")
			uidTemp = int(lineSplit[0][1:])
			if uidTemp in users: 
				if uidTemp == user: 
					payment = payment + "|" + lineSplit[1].rstrip()
				else: 
					user = uidTemp
					payment = lineSplit[1].rstrip()
				self.users[user]["Payment"] = payment
		myfile.close()
					


#returns a list of user ids
	def get_users(self):
		return self.users.keys()	
			
#returns a list of a specfic user
	def get_user(self, uid): 
		uid = int(uid)
		if uid in self.get_users():	
			userList = [ self.users[uid]["Smoker"], self.users[uid]["Drink Level"], self.users[uid]["Ambience"], self.users[uid]["Transport"], self.users[uid]["Budget"], self.users[uid]["Cuisine"], self.users[uid]["Payment"]]
			return userList
		else: 
			return None 	

#add a user to the dictionary
	def set_user(self, uid, user):
		uid = int(uid)
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
			self.users[int(uid)] = userDict

#delete a specific user
	def delete_user(self, uid):
		if int(uid) in self.get_users():
			del self.users[int(uid)]

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
			self.restaurants[int(lineSplit[0])] = {"Location": location,  "Name": lineSplit[4],"Alcohol": lineSplit[11], "Smoking Area": lineSplit[12], "Dress Code": lineSplit[13], "Price": lineSplit[15], "URL": lineSplit[16], "Sun;": None, "Sat;": None, "Mon;Tue;Wed;Thu;Fri;": None, "Payment Accepted": None, "Cuisine": None, "Parking": None}
		myfile.close()
		myfile = open("data/restaurantPaymentAccepted.csv")
		firstLine = myfile.readline()
		payment = ""
		restaurant = -1
		restaurants = self.get_restaurants()
		for line in myfile: 
			lineSplit = line.split(",")
			ridTemp = int(lineSplit[0])
			if ridTemp in restaurants: 	
				if ridTemp == restaurant: 
					payment = payment + "|" + lineSplit[1].rstrip()
				else:
					restaurant = ridTemp
					payment = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Payment Accepted"] = payment 
		myfile.close()
		myfile = open("data/restaurantCuisine.csv")
		firstLine = myfile.readline()
		restaurant = -1
		cuisine = ""
		for line in myfile:
			lineSplit = line.split(",")
			ridTemp = int(lineSplit[0])
			if ridTemp in restaurants:
				if ridTemp  == restaurant:	
					cuisine = cuisine + "|" + lineSplit[1].rstrip()
				else: 
					restaurant = ridTemp
					cuisine = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Cuisine"] = cuisine
		myfile.close()
		myfile = open("data/restaurantParking.csv")
		firstLine =  myfile.readline()
		restaurant = -1
		parking = ""
		for line in myfile: 
			lineSplit = line.split(",")
			ridTemp = int(lineSplit[0])
			if ridTemp in restaurants:
				if ridTemp == restaurant: 
					parking = parking +"|"+ lineSplit[1].rstrip()
				else: 	
					restaurant = ridTemp
					parking = lineSplit[1].rstrip()
				self.restaurants[restaurant]["Parking"] = parking
		myfile.close()
		myfile = open("data/restaurantHours.csv")
		firstLine =  myfile.readline()
		#if multiple entries, use the last entry in the file
		#if multiple times in an entyr, use first time given 
		for line in myfile: 
			lineSplit = line.split(",")
			if int(lineSplit[0]) in restaurants:
				time = lineSplit[1]
				if ";" in time: 
					time = lineSplit[1].split(";")[0]
				self.restaurants[int(lineSplit[0])][lineSplit[2].rstrip()] = time
		myfile.close()
#returns a list of keys of restaurants
	def get_restaurants(self):
		return self.restaurants.keys()
		
#returns an array of a specific restaurant 
	def get_restaurant(self, rid):
		rid = int(rid)
		if rid in self.get_restaurants():
			restaurantList  = [list(self.restaurants[rid]["Location"].values()), self.restaurants[rid]["Name"], self.restaurants[rid]["Alcohol"], self.restaurants[rid]["Smoking Area"], self.restaurants[rid]["Dress Code"], self.restaurants[rid]["Price"], self.restaurants[rid]["URL"], self.restaurants[rid]["Payment Accepted"], self.restaurants[rid]["Cuisine"], self.restaurants[rid]["Parking"], self.restaurants[rid]["Sun;"], self.restaurants[rid]["Sat;"], self.restaurants[rid]["Mon;Tue;Wed;Thu;Fri;"]]
			return restaurantList
		else:	
			return None
						
#sets a restaurant to input given which is a restaurant and a given id 
	def set_restaurant(self, rid, restaurant):
		rid = int(rid)
		if rid in self.get_restaurants(): 
			self.restaurants[rid]["Location"]["Latitude"] = restaurant[0][0]
			self.restaurants[rid]["Location"]["Longitude"] = restaurant[0][1]
			self.restaurants[rid]["Location"]["Address"] = restaurant[0][2]
			self.restaurants[rid]["Location"]["City"] = restaurant[0][3]
			self.restaurants[rid]["Location"]["State"]= restaurant[0][4]
			self.restaurants[rid]["Location"]["Country"] = restaurant[0][5]
			self.restaurants[rid]["Location"]["Zipcode"] = restaurant[0][6]
			self.restaurants[rid]["Name"]= restaurant[1]
			self.restaurants[rid]["Alcohol"] = restaurant[2]
			self.restaurants[rid]["Smoking Area"] = restaurant[3]
			self.restaurants[rid]["Dress Code"] = restaurant[4]
			self.restaurants[rid]["Price"] = restaurant[5]
			self.restaurants[rid]["URL"] = restaurant[6]
			self.restaurants[rid]["Payment Accepted"] = restaurant[7]
			self.restaurants[rid]["Cuisine"] = restaurant[8]
			self.restaurants[rid]["Parking"] = restaurant[9]
			self.restaurants[rid]["Sun;"] = restaurant[10]
			self.restaurants[rid]["Sat;"] = restaurant[11]
			self.restaurants[rid]["Mon;Tue;Wed;Thu;Fri;"] = restaurant[12]
		else: 
			location = {"Latitude": restaurant[0][0], "Longitude": restaurant[0][1], "Address": restaurant[0][2], "City": restaurant[0][3], "State": restaurant[0][4], "Country": restaurant[0][5], "Zipcode": restaurant[0][6]}
			restDict = {"Location": location, "Name": restaurant[1], "Alcohol": restaurant[2], "Smoking Area": restaurant[3], "Dress Code": restaurant[4], "Price": restaurant[5], "URL": restaurant[6], "Payment Accepted": restaurant[7], "Cuisine": restaurant[8], "Parking": restaurant[9], "Sun;":restaurant[10], "Sat;":restaurant[11], "Mon;Tue;Wed;Thu;Fri;": restaurant[12]}
			self.restaurants[rid] = restDict
#delete a given restaurant
	def delete_restaurant(self, rid):
		if int(rid) in self.get_restaurants(): 
			del self.restaurants[int(rid)]

	def load_ratings(self):
		self.ratings.clear()
		f = open("data/ratings.csv")
		firstLine = f.readline()
		for line in f:
			info = line.rstrip().split(",")
			uid = int(info[0][1:])
			rid = int(info[1])
			rating = float(info[2])
			foodrating = float(info[3])
			servrating = float(info[4])
			if rid not in self.ratings.keys():
				self.ratings[rid] = dict()
			if uid not in self.ratings[rid].keys():
				self.ratings[rid][uid] = []
				self.ratings[rid][uid].append(rating)
				self.ratings[rid][uid].append(foodrating)
				self.ratings[rid][uid].append(servrating)
			#print(rid)
			#print(self.ratings[
		f.close()
		#print(self.ratings)
		
# return the average overall ratings of a restaurant
	def get_rating(self, rid):
		total = 0
		ftotal = 0
		stotal = 0
		numRatings = 0
		rid = int(rid)
		if rid in self.ratings:
			for uid in self.ratings[rid]:
				rating = self.ratings[rid][uid][0]
				frating = self.ratings[rid][uid][1]
				srating = self.ratings[rid][uid][2]
				numRatings = numRatings + 1
				total = float(total + rating)
				ftotal = float(ftotal + frating)
				stotal = float(stotal + srating)
			average = total / float(numRatings)
			faverage = ftotal / float(numRatings)
			saverage = stotal / float(numRatings)
			return [average, faverage, saverage]
		else:
			return 0
	

# if user exists, allow them to add or change a rating for a given rid
# given uid, rid, and a list containing overall rating, service rating,
# and food rating
	def set_user_restaurant_ratings(self, uid, rid, ratings):
		#if rid not in self.ratings:
			#self.ratings[rid] = {}
		self.ratings[int(rid)][int(uid)] = ratings

	def set_filters(self, pricepoint, cuisinetype, dresscode, paymenttype):
		self.filters["Price"] = pricepoint
		self.filters["Cuisine"] = cuisinetype
		self.filters["Dress Code"] = dresscode
		self.filters["Payment Accepted"] = paymenttype

	def filter_restaurants(self):
		
		matches = self.restaurants
		temp = dict(matches)
		if self.filters["Price"] != "None":
			for rid in matches:
				if matches[rid]["Price"] != self.filters["Price"] and int(rid) in temp:
					del temp[int(rid)]
			matches = dict(temp)
		if self.filters["Cuisine"] != "None":
			for rid in matches:
				cuisineString = matches[rid]["Cuisine"] 
				if cuisineString != None:
					cuisines = cuisineString.split("|")
					for cuisine in cuisines:
						if cuisine != self.filters["Cuisine"] and int(rid) in temp:
							del temp[int(rid)]
			matches = dict(temp)
		if self.filters["Dress Code"] != "None":
			for rid in matches:
				if matches[rid]["Dress Code"] != self.filters["Dress Code"] and int(rid) in temp:
					del temp[int(rid)]
			matches = temp
		if self.filters["Payment Accepted"] != "None":
			for rid in matches:
				paymentString = matches[rid]["Payment Accepted"]
				if paymentString != None:
					payments = paymentString.split("|")
					for payment in payments:
						if payment != self.filters["Payment Accepted"] and int(rid) in temp:
							del temp[int(rid)]
			matches = temp

		return matches

	def get_prices(self):
		prices = ["None"]
		for rid in self.restaurants:
			if self.restaurants[rid]["Price"] not in prices:
				prices.append(self.restaurants[rid]["Price"])
		return prices

	def get_cuisines(self):
		cuisines = ["None"]
		for rid in self.restaurants:
			if self.restaurants[rid]["Cuisine"] not in cuisines:
				cuisines.append(self.restaurants[rid]["Cuisine"])
		return cuisines

	def get_dresscode(self):
		dresscodes = ["None"]
		for rid in self.restaurants:
			if self.restaurants[rid]["Dress Code"] not in dresscodes:
				dresscodes.append(self.restaurants[rid]["Dress Code"])
		return dresscodes

	def get_payments(self):
		payments = ["None"]
		for rid in self.restaurants:
			paymentString = self.restaurants[rid]["Payment Accepted"]
			if paymentString != None:
				paymentset = paymentString.split("|")
				for payment in paymentset:
					if payment not in payments:
						payments.append(payment)
		return payments


	'''
	def filter_by_price(self, pricepoint):
		matches = []
		for rid in self.restaurants:
			if self.restaurants[rid]["Price"] == pricepoint:
				matches.append(rid)
		return matches

	def filter_by_cuisine(self, cuisinetype):
		matches = []
		for rid in self.restaurants:
			cuisineString = self.restaurants[rid]["Cuisine"]
			if cuisineString != None:
				cuisines = cuisineString.split("|")
				for cuisine in cuisines:
					if cuisine == cuisinetype:
						matches.append(rid)
		return matches

	def filter_by_dresscode(self, dresscode):
		matches = []
		for rid in self.restaurants:
			if self.restaurants[rid]["Dress Code"] == dresscode:
				matches.append(rid)
		return matches

	def filter_by_payment(self, paymenttype):
		matches = []
		for rid in self.restaurants:
			paymentString = self.restaurants[rid]["Payment Accepted"]
			if paymentString != None:
				payments = paymentString.split("|")
				for payment in payments:
					if payment == paymenttype:
						matches.append(rid)
		return matches
	'''
