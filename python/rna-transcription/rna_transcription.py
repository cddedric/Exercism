def to_rna(inputString):
	outputString = ''
	for character in inputString:
		if character == 'G':
			outputString += 'C'
		elif character == 'C':
			outputString += 'G'
		elif character == 'T':
			outputString += 'A'
		elif character == 'A':
			outputString += 'U'
		else:
			return ''
	
	return outputString
"""
	g<->c
	t->a
	a->u 
"""