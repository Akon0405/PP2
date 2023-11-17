def counter(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

user_string = input()
upper, lower = counter(user_string)
print(upper)
print(lower)
