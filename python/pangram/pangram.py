def is_pangram(inputString):
	count = {}							#init dictionary
	inputString = inputString.lower()	#lowercase string for easier handling
	
	for character in inputString:		#loop through input string
		if character.isalpha():			#check each character in input string to see if alpha
			count[character] = True		#adds character to dictionary and sets value to true
										#if already in dictionary, sets value of true to true 
	return len(count) == 26				#if dictionary == 26, all letters seen and is pangram, otherwise false