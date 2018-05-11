#imports
from py_classes import *

print "Welcome to The DM's Screen. Here, you will find all sorts of things to help in maintaining your campaign, or multiple at once."
print "There isn't too much right now, but many things are under progress. There is still plenty more planned for the future."
print ""

#and let the menuing begin
while True:
	print "<<Main Menu>>"
	print "Please select the number of which action you would like to do"
	print "1. Organization Management"
	print "2. Character Management"
	print "3. Exit"
	choice = raw_input("--->")
	print ""

	#organization management
	if choice == "1":
		#doing a little bit of prep for organization management
		orgs_file = open("organization_master_list.txt", "r")
		orgs = []

		#getting rid of the newline characters
		for line in orgs_file:
			orgs.append(line.rstrip())
		
		#making sure to close the file
		orgs_file.close()

		#running the Organization menu
		while True:
			print "<<Organization Management>>"
			print "Please select the number of which action you would like to perform"
			print "1. Create a new organization"
			print "2. Change an organization's name"
			print "3. See the list of all current Organizations"
			print "4. Remove an Organization"
			print "5. Return to Main Menu"
			choice = raw_input("--->")
			print ""

			#creating an organization
			if choice == "1":
				#loop until a valid name is entered
				while True:	
					name = raw_input("What is the name of this new organization: ")
					print ""
					name = sanitize_string(name)
					
					#checking for duplicate org names
					if name in orgs:
						choice =  raw_input("Sorry, but " + name + " is already in use. Would you like to overwrite, try a different name, or cancel creation (o/d/c): ")
						print ""
						duplicate = True

					else:
						duplicate = False

					#check choice if there was a duplicate
					if duplicate:
						#overwrites with new organization
						if choice == "o":
							current_org = Organization(name, False)
							current_org.remove_org()
							current_Org = Organization(name, True)

						#cancels creation
						elif choice == "c":
							break

					
					else:
						current_org = Organization(name, True)
						orgs.append(name)
						print "Organization " + name + " created! Returning to organization management."
						print ""
						break

			#changing an org's name
			elif choice == "2":
				pass

			#displays each organization
			elif choice == "3":
				print "Organizations:"
				for org in orgs:
					print org
				print ""

			#deleting an organization
			elif choice == "4":
				name = raw_input("Which organization would you like to delete: ")
			
			#go back to main menu
			elif choice == "5":
				break

			#repeat for improper command
			else:
				print "Sorry, didn't get that"
				print ""

	#character management
	elif choice == "2":
		pass

	#exit the program
	elif choice == "3":
		print "Thank you for using the DM's Screen."
		break

	else:
		print "Sorry, didn't get that"
		print ""
