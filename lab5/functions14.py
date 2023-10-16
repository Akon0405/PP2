import math

def filter_prime(arr):
    return list(filter(lambda x : is_prime(x), arr))

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print(filter_prime([10,21,3,8,9,11,44,62,100,19]))
