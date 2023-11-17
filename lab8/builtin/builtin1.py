import functools

def multiply_list(numbers):
    result = functools.reduce(lambda x, y: x * y, numbers)
    return result

number_list = [1, 2, 3, 4, 5]
result = multiply_list(number_list)

print(result)
