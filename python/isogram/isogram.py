def is_isogram(inputString):
	count = {}									#init dictionary for character counting
	inputString = inputString.lower()
	for character in inputString:				# loop through all characters given to it
		if character.isalpha():					#check if characters given are a-z or A-Z
			count.setdefault(character,0)		#add lowercase of given character to dictionary
			count[character] = count[character] +1	#add 1 for each time a character is found and keep track of occurrences 
			if count[character] >= 2:			#if more than 1 of same character found, not isogram
				return False					#therefore, return False
	return True									#empty strings, non alphabetical strings and isograms are isograms, return True