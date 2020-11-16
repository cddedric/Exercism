def distance(firstString,secondString):
	if len(firstString) != len(secondString):
		raise ValueError
	hamming = 0
	for charIndex in range(len(firstString)):
		if firstString[charIndex] != secondString[charIndex]:
			hamming += 1
	
	return hamming