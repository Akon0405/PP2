import re

def insert_spaces(input_string):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result

# Test the function
input_string = input('Input string:')
result = insert_spaces(input_string)
print(result)
