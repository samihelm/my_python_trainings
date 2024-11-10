input_string = input("please enter a string: ")
letters = ""
digits = ""
for char in input_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
print("letters: ", letters)
print("digits: ", digits)
 
