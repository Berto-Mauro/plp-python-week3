full_name = input("Enter your full name: ")

name_parts = full_name.split()

if len(name_parts) >= 2:
    print("Hello, " + "! Nice to meet you.")
else: 
    print("Please enter your full name, including your first name and last name.")