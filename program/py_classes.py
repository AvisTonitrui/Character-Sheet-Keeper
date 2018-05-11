#imports needed for the classes to work
import os
import shutil
from py_functions import *

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

class Organization:
	
	#intializing the class
	def __init__(self, name, new):
		#setting the name of the organization
		self.name = name
		
		#creating the organization file structure if it is a new organization
		if new:
			#making the organization directory
			os.makedirs(self.name)

			#creating the players list
			players_file = open(self.name + "/player_list.py", 'w')
			players_file.write("#" + self.name + "'s players:")
			players_file.close()

			#adding to the organization master list
			org_file = open("organization_master_list.txt", 'a')
			org_file.write(self.name)
			org_file.close()

			#initializing the remaining variables
			self.players = []

		#initialization for an existing organization
		else:
			pass

	#changing the organization's name
	def name_change(self):
		pass

	#deleting the organization
	def delete_org(self):
		#removes the folder for the organization
		shutil.rmtree("/" + self.name, ignore_errors = True)

		#removes the name from the master list
		#opens the file to read in order to get all the organizations
		master_list = open("organization_master_list.txt", "r")
		orgs = []

		#getting rid of the newline characters
		for line in master_list:
			orgs.append(line.rstrip())

		#closing and removing the file
		master_list.close()
		os.remove("organization_master_list.txt")

		#removes the instance from this list
		orgs.remove(self.name)

		#writes the new set to the folder
		master_list = open("organization_master_list.txt", "a")

		for org in orgs:
			master_list.write(org)

		#closes the file
		master_list.close()
		
