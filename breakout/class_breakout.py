
def find_dupe():
    new_list = []
    num_list = [ 1, 2, 3, 4, 4, 5 ]
    for number in num_list:
        if number not in new_list:
            new_list.append(number)
        else:
            return number
    print(number)
