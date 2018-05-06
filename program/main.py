#imports
from py_classes import *

print "Welcome to The DM's Screen. Here, you will find all sorts of things to help in maintaining your campaign, or multiple at once."
print "There isn't too much right now, but many things are under progress. There is still plenty more planned for the future."
print ""

#and let the menuing begin
while True:
	print "Please select the number of which action you would like to do"
	print "1. Organization management"
	print "2. Character management"
	print "3. Exit"
	choice = raw_input("--->")

	#organization management
	if choice == "1":
		pass

	#character management
	elif choice == "2":
		pass

	#exit the program
	elif choice == "3":
		print "Thank you for using the DM's Screen."
		break

	else:
		print "Sorry, didn't get that"
