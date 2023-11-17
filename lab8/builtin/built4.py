def palindrome(string):
    if string == ''.join(reversed(string)):
        return True
    else: return False

string = input()
if palindrome(string):
    print("Yes")
else:
    print("No")
