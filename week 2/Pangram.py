import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    s = set(s) 
    return alphabet.issubset(s) 

# Taking user input
text = input("Enter a string: ")


if is_pangram(text):
    print("It's a pangram!")
else:
    print("Not a pangram.")