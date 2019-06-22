'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
def two_sum(lis, target):
    first = None
    second = None

    for num in lis:
        desired = target - num

        if desired in lis:
        second = lis.index(desired)

        if num + desired == target:
            first = lis.index(num)
        return [first, second]

    return 'None Found'

answer = two_sum([2, 11, 15], 9)
print(answer)
