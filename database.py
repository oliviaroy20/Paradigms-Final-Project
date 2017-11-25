class database.py: 
	def __init__(self): 
		self.users = dict()
	
	def load_users(self): 
		self.users.clear()
		myfile = open("data/userProfile.csv")
		for line in myfile: 
			lineSplit = line.split(",")
			self.users[lineSplit] = {"Smoker": lineSplit[3], "drink_level" : lineSplit[4], "ambience" : lineSplit[5], "transport" : lineSplit[6], "budget": lineSplit[15]}
		myfile.close()
		myfile = open("data/userCuisine.csv")
		user = ""
		cuisine = "" 
		for line in myfile: 
			lineSplit = line.split(",")
			if user == lineSplit[0]:
				cuisine = cuisine + "|"+ lineSplit[1]
			else:
				self.users[user] = dict()
				self.users[user]["cuisine"] = cuisine
				user = lineSplit[0]
				cuisine = "" 
		myfile.close()
		
