

def two_array_two_sum(first_list, second_list, target):
    '''Iterate both arrays simultaneously'''
    match = None
    compliment = float('inf')

    # iterating through the first list
    for first_num in first_list:

        # iterating through second list
        for second_num in second_list:

            # set difference equal the sum of first num and second num subtracted from the target
            difference = abs(target - (first_num + second_num))

            # if the difference is less than the compliment
            if difference < compliment:

                # the match is equal to the first num and second num
                match = (first_num, second_num)

                # set compliment equal to the difference
                compliment = difference
                
    return match



first_list = [12, 11, 10, 17, 16, 13]
second_list = [3, 7, 4, 14, 6]
target = 20

print('Two Array Two Sum:')
print(two_array_two_sum(first_list, second_list, target))