def calculate_fb(val):
    if val % 3 == 0:
        if val % 5:
            return "FizzBuzz"
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    else:
        return val

def fizzbuzz(start, end):
    curr = start
    if curr > end:
        return
    yield calculate_fb(curr)
    yield from fizzbuzz(curr+1, end)

print(list(fizzbuzz(5, 20)))