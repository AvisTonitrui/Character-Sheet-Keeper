#these are the generic functions used in many parts of the program

#sanitizes a string for proper file naming
def sanitize_string(string):
	valid_characters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_"]
	final = string
	index = 0
	indecies = []
	
	for character in string:
		if character not in valid_characters:
			indecies.insert(0, index)
		
		index += 1

	for index2 in indecies:
		if string[index2] == " ":
			string[index2] = "_"
		else:
			string[index2] = ""

	return string
