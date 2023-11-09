import re

def split_at_uppercase(input_string):

    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result

input_string = input("Input string:")
result = split_at_uppercase(input_string)
print(result)
