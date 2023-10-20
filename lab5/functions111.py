def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

phrase1 = "A man a plan a canal Panama"
phrase2 = "racecar"
phrase3 = "hello world"

print(is_palindrome(phrase1))  # True
print(is_palindrome(phrase2))  # True
print(is_palindrome(phrase3))  # False
