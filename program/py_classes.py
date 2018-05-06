#These are the classes used

class Player:

	#for importing the info from the character
	def imp(self):
		#open the file where all the info is located
		file = open(self.organization + "/" + self.name, 'r')

		#close the file when we're done
		file.close()
	
	#for creating a character from scratch
	def crea(self):
		pass

	#initializing the class
	def __init__(self, organization, name, new):
		#setting the organization and name
		self.organization = organization
		self.name = name

		if new:
			crea()
		else:
			imp()
