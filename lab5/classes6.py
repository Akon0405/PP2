def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [2, 3, 5, 7, 9, 11, 12, 13, 17, 19, 23, 29]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime Numbers:", prime_numbers)
