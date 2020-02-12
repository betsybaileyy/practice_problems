"""given two arrays of numbers and a target value
find a number from each array whose sum is closest to t"""

def closest_pair_slow(first_list, second_list, target):
    perf_pair = [first_list[0], second_list[0]]
    for i in first_list:
        for j in second_list:
            if abs(target - sum(perf_pair)) > abs(target - i - j):
                perf_pair = [i, j]
    return perf_pair


def closest_pair(first_list, second_list, target):
	first_list = first_list[:]
	second_list = second_list[:]
	first_list.sort()
	second_list.sort()

	index_first_list = 0
	index_second_list = len(second_list) - 1

	perf_pair = [first_list[index_first_list], second_list[index_second_list]]

	while index_first_list <= len(first_list) - 1 and index_second_list >= 0:
		curr_pair = [first_list[index_first_list], second_list[index_second_list]]
		if abs(sum(perf_pair) - target) > abs(sum(curr_pair) - target):
			perf_pair = curr_pair

		if sum(curr_pair) < target:
			index_first_list += 1

		elif sum(curr_pair) > target:
			index_second_list -= 1

	
		else:
			break

	return perf_pair


first_list = [5, 6, 2, 13, 19, 7, 21]
second_list = [3, 17, 4, 14, 1]
target = 20
print(closest_pair(first_list, second_list, target))