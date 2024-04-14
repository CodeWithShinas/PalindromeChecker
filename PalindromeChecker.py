# AdolNerdHub Shinas Vishwagith whatsapp +94725222161
# https://github.com/CodeWithShinas
'''Write a function that takes a string as input and returns True if the string is 
a palindrome (reads the same forwards and backwards), otherwise returns False.'''

def is_palindrome(text):
    text=text.lower()
    text="".join(char for char in text if char.isalnum())

    return text == text[::-1]

print(is_palindrome("Was it a car or a cat he saw?"))