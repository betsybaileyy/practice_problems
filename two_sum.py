# Given an list of numbers and a target value
# find two numbers whose sum is t. 

# shoutout to Nolan for helping with this one!

def two_sum(list, t):
	#valid_int holds valid numerical complements.
	valid_int = set()

	# crawl through the list by each num
	for num in list:
		# whats this number's numerical complement in order to reach the sum?
		complement = t - num
		# is this number a numerical complement of another?
		if complement in valid_int:
			return complement, num
		else:
			# if not, add the needed number to valid_int
			valid_int.add(num)

	# no matches
	return None

# Test
list = [5, 3, 6, 8, 2, 4, 7]
t = 10
print(two_sum(list, t))
