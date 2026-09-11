# BUG: The closing quotation mark was missing, causing a SyntaxError. I added the missing quotation mark.
print("Welcome to the Bug Hunt!")
name = input("What is your name? ")
# BUG: The variable name was misspelled as "nmae". I corrected it to "name".
print("Nice to meet you, " + name)
# BUG: The age from input() was a string, so it could not be added to 1. I converted it to an integer using int().
age = int(input("How old are you? "))

print("Next year you will be " + str(age + 1))