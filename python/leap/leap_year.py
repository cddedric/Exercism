"""
def is_leap_year(inputYear):

	if inputYear % 4:
		if inputYear % 100:
			if inputYear % 400:
				return True			#divisible by 400, making it a leap year
			else:
				return False		#divisible by 100 but not 400, not leap year
		return True					#divisble only by 4, leap year
	else:
		return False				#not divisible by 4, definitely not a leap year

		
"""


def is_leap_year(inputYear):
	if inputYear % 400 ==0:
		return True
	elif inputYear % 100 ==0:
		return False
	elif inputYear % 4 ==0:
		return True
	else:
		return False