#                       Exercise 3: Biography - 25 Mark
# In this exercise, you'll create a program that stores and prints your name, hometown, 
#               and age to the console using a Python dictionary.

#     Steps: 
#     1 Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#     2 Print the values on separate lines using a single print() statement.
#     3 Use variables with appropriate data types for each piece of information.

# Advanced Requirements: Have the user input their name, hometown, and age instead of hardcoding the values. 
# Try giving both your first and second name when asked for your name. What happens? 
# How can you handle multiple words in Python? Test the program by entering a string value for age 
# (e.g., "twenty"). What happens? How can you prevent this issue?

#Program:

name = input("Enter your name full name(Your first and last name): ") 
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: "))

# This gets the users information for their name, hometown and age

print(f"Name: {name}\nHometown: {hometown}\nAge: {age}")

# This prints it and creates a dictionary stating the users name, hometown and age.

# Output for this code: 
# Enter your name full name(Your first and last name): Achilles Maling
# Enter your hometown: Phillipines, Antipolo
# Enter your age: 19
# Name: Achilles Maling
# Hometown: Phillipines, Antipolo
# Age: 19

# IF the user inputs a string value (eg: twenty) for age, a neccessary code needs to be given in order
#                 to tell the user to input a valid number for their age

#Program: 
name = input("Enter your name full name(Your first and last name): ") 
hometown = input("Enter your hometown: ")

while True: 
    age = input("Enter your age: ")  
    if age.isdigit(): 
        age = int(age) 
        break  
    else:
        print ("Please enter a valid number for your age")

print(f"Name: {name}\nHometown: {hometown}\nAge: {age}")

#Output for this code above:
# Enter your name full name(Your first and last name): Achilles Maling
# Enter your hometown: Antipolo
# Enter your age: Nineteen
# Please enter a valid number for your age
# Enter your age: 19
# Name: Achilles Maling
# Hometown: Antipolo
# Age: 19


