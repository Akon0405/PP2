import re

def snake_to_camel(match):
    return match.group().replace('_', '').capitalize()

x = input("Enter snake_case string: ")
camel_case_content = re.sub(r'_([a-z])', snake_to_camel, x)

print(camel_case_content)
