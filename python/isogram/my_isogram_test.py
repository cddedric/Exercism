def is_isogram(inputString):
	alphaOnlyString = ''					      #init string for own sanity
	for character in inputString:				# loop through string
		if character.isalpha():					# check if character at point is a-z or A-Z
			alphaOnlyString += character		# if character, add to string

	# alphaOnlyString is either letters or nothing at all
	if alphaOnlyString == '':              #string is empty due to no alphabetical characters present
		return False                          #therefore, return false, not isogram
	else:
		alphaOnlyString = alphaOnlyString.lower() #convert character string to lowercase for comparison
    
    # alphaOnlyString is now only characters and lowercase
    
	count = {}
    
	for character in alphaOnlyString:
		count.setdefault(character,0)
		count[character] = count[character] +1  #dictionary for characters and number of times it appears
		if count[character] >= 2:
			return False
        
	return True