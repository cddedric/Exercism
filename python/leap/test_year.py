from leap_year import is_leap_year

def test_year():
	inputYear = input("input year: ")
	inputYear = int(inputYear)
	if is_leap_year(inputYear):
		print('true')
	else:
		print('false')
		
test_year()