class _restaurant_database: 
	def __init__(self): 
		self.users = dict()
	
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
			self.users[lineSplit[0]] = {"Smoker": lineSplit[3], "Drink Level" : lineSplit[4], "Ambience" : lineSplit[5], "Transport" : lineSplit[7], "Budget": lineSplit[17], "Cuisine": None, "Payment": None}
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
				self.users[user]["Cuisine"] = cuisine
				
	
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
				self.users[user]["Payment"] = payment
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













