# Assessment 1 Code lab Module by Achilles Ratuiste Maling
This repository contains a series of exercises given by the tutor and done by the student. Basic Python Exercises are given throughout this repository such as if-else exercises, python loops, arithmetic sequences, functions etc. These exercises are used to improve coding knowledge and to show how to further elaborate and improve a code. In some exercises, multiple programs are given emphasising the difference between the normal program and an advanced program. These exercises are based on real-life situations in which may be useful in the near future.

# List of Exercises
  - Exercise #1: Coding is Cool (01Codingiscool.py)
  - Exercise #2: Simple Sums (02SimpleSums.py)
  - Exercise #3: Biography (03Biography.py)
  - Exercise #4: Primitive Quiz (04.PrimitiveQuiz.py)
  - Exercise #5: Days Of The Month (05.DaysOfTheMonth.py)
  - Exercise #6: Brute Force Attack (06.BruteForceAttack)
  - Exercise #7: Some Counting (07.SomeCounting.py)
  - Exercise #8: Simple Search (08.SimpleSearch.py)
  - Exercise #9: Hello (09.Hello.py)
  - Exercise #10: Is it Even (10.IsItEven.py)

## Exercise 1: Coding is Cool- 10 Marks

Fill in the blanks in the Python code below to output the phrase **"Coding is Cool"** to the console using variables and string concatenation.

### Fill in the blanks below
### Result:
```python
word1 = ('Coding ')
word2 = ('is ')
word3 = ('Cool ')
print ( word1 + word2 + word3 )

#Explanation: In this code, it sets word1 to "Coding ", word2 to "is ", and word3 to "Cool ". It then concatenates
#             these variables with the + operators and prints the resulting string to the terminal. yes


#Output = Coding is Cool

```

__________________________________________________________________________________

## Exercise 2: Simple Sums - 15 Marks

In this exercise, you will create and work with integer variables, perform arithmetic operations, and print the result to the console.

### Steps:
1. Declare a variable and initialize it with the integer value `8`.
2. Declare a second variable and initialize it with the integer value `10`.
3. Declare a third variable that stores the sum of first two numbers.
4. Print the value of the sum to the console.

### Result:
```python
integer1 = 8
integer2 = 10

sum_result = (integer1 + integer2)

print(sum_result)

# Explanation: In this code, it emphasises integer1 as 8 and integer2 as 10. 
#              It then stores it in sum_result and calculates their sum, which is
#              printed to the terminal. Output will be 18

# Output = 18

```

__________________________________________________________________________________

## Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

### Result:
```python
Program: 
name = input("Enter your name full name(Your first and last name): ") 
hometown = input("Enter your hometown: ")

while True: 
    age = input("Enter your age: ")  
    if age.isdigit(): # checks whether the age is an integer or not
        age = int(age) # converts the given string value to an integer
        break  # this exits the loop if the user has entered a proper number
    else:
        print ("Please enter a valid number for your age")

print(f"Name: {name}\nHometown: {hometown}\nAge: {age}")

#Output for this code above:
# Enter your name full name(Your first and last name): Achilles Maling
# Enter your hometown: Antipolo, Philippines
# Enter your age: Nineteen
# Please enter a valid number for your age
# Enter your age: 19
# Name: Achilles Maling
# Hometown: Antipolo, Philippines
# Age: 19
```


__________________________________________________________________________________


## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

### Result:
```python
#Program

answer = input("What is the capital of France? ")

if answer.lower() == "paris": #This allows the user to input the word 'paris' in any form (eg: Paris, PaRis)

    print ("The answer you have given is correct. ")

else:

    print ("The answer you have given is wrong. ")

#output: What is the capital of France? pAris
#        The answer you have given is correct.    
#        What is the capital of France? berlin
#        The answer you have given is wrong.     

#Guess the Capital of Each City

Quiz = {
    ("What is the capital of France?", "Paris"), #1
    ("What is the capital of Germany?", "Berlin"), #2
    ("What is the capital of Italy?", "Rome"), #3
    ("What is the capital of Spain?", "Madrid"), #4
    ("What is the capital of the Netherlands?", "Amsterdam"), #5
    ("What is the capital of Greece?", "Athens"), #6
    ("What is the capital of Portugal?", "Lisbon"), #7
    ("What is the capital of Belgium?", "Brussels"), #8
    ("What is the capital of Switzerland?", "Bern"), #9
    ("What is the capital of Belgium?", "Brussels"), #10
}

#Creates a Dictionary which acts like a Quiz

print ("Welcome to Guess the Capital of Each City" )

for Quiz, correct_answer in Quiz: # The 'for' loop goes throught each question, asking and checking if the answer is correct
    answer = input(Quiz + " ")
    if answer.lower() == correct_answer.lower(): #This allows the user to input the word 'paris' in any form (eg: Paris, PaRis)

        print ("The answer you have given is correct. ")

    else: 
        print("The answer you have given is wrong. ")

print ("That is the end of the quiz, thank you. ")

```


___________________________________________________________________________________

## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

### Result:
```python
## Program

month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
    # Creates a dictionary in which tells how many days are in each month

month = int(input("Enter the month number (1-12): ")) #This asks the user to input the month number that they want

if month < 1 or month > 12:
    print ("The month number that was given is invalid, please try again and enter a number between 1 and 12")

else: 
    print (f"This month has {month_days[month]} days.")

# Explanation: The program above emphasises an if else statement in which asks the user to input a month number and 
#              it would output the given month number that was stated in the dictionary. If the number is invalid, it would
#              inform the user that the number given is invalid

# Output: Enter the month number (1-12): 3
#         This month has 31 days. 

## Advanced Program 

month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
    # Creates a dictionary in which tells how many days are in each month

month = int(input("Enter the month number (1-12): ")) #This asks the user to input the month number that they want

if month < 1 or month > 12: #This checks whether the user inputs a valid number or not (1-12)
    print ("The month number that was given is invalid, please try again and enter a number between 1 and 12")

else: #This part asks the user if the current year is a leap year or not

    if month == 2: #Checks if the input is February or not

        leap_year = input("Is the current year a leap year? (yes or no): ")

        if leap_year == "yes":
            print ("Then the month of February has 29 days")

        else:
            print ("Then the month of February still has 28 days")

    else:
        print (f"This month has {month_days[month]} days.")

# Explanation: This advanced program asks the user to input a month (1-12). If the user inputs 2 which is February,
#              the program then asks the user whether if the current year is a leap year or not. If it is, the program 
#              outputs a different number for the month of February. 

# Output: Enter the month number (1-12): 2
#         Is the current year a leap year? (yes or no): yes
#         Then the month of February has 29 days
```


____________________________________________________________________________________

## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

### Result:
```python
# Program

correct_password = "12345"

while True: # The 'while true' creates an infinite loop as it will keep asking for the user's correct password
    enter_password = input ("Enter Your Password: ")

    if  enter_password == correct_password: 
        print ("Logged In! Please wait...")

        break   #This break exits the loop. This means the user has entered the correct password.

    else:
        print ("Incorrect Password, please try again :(")

# Explanation: In this program, it presents a password system in which asks the user for their password to log them in to their system or to whatever 
#              to they are trying to get access to. It showcases a python loop (infinite while loop) as it gives the user infinite chances in attempting
#              to input their password. 

# Output:
#  Enter Your Password: 232
#  Incorrect Password, please try again: 
#  Enter Your Password: 12345
#  Logged In! Please wait...

# Advanced Program

correct_password = "12345"

maximum_attempts = 5
attempts = 0
# This shows how many attempts the user can make

while attempts < maximum_attempts:
    enter_password = input("Enter Your Password: ")
    attempts += 1 #This makes the attempts lessen everytime the user enters the wrong password

    if enter_password == correct_password:
        print("Logged In! Please wait...")
        break
    
    else:
        remaining_attempts = maximum_attempts - attempts
        
        if remaining_attempts > 0:
            print(f"The password is incorrect . You have {remaining_attempts} attempt(s) left")
        
        else:
            print(f"You have no more remaining attempts, authorities have been alerted")

# This program uses a while loop with an if-else statement as the while loop repeats until the user either gets the 
# password right or uses all the attempts. 

# Output:
# Enter Your Password: 12345 
# Logged In! Please wait...
# Enter Your Password: 12  
# The password is incorrect . You have 4 attempt(s) left
# Enter Your Password: 234
# The password is incorrect . You have 3 attempt(s) left
# Enter Your Password: 34
# The password is incorrect . You have 2 attempt(s) left
# Enter Your Password: 34
# The password is incorrect . You have 1 attempt(s) left
# Enter Your Password: 3
# You have no more remaining attempts, authorities have been alerted

```


_____________________________________________________________________________________

## Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*

### Result:
```python
# Program

# 0 to 50 in increments of 1
print("Starting to count up from 0 to 50... ")
for int in range(0, 51): #This will start from 0 to 50
    print (int)
print("Done!")

# 50 to 0 in decrements of 1
print("Starting to count down from 50 to 0...")
for int in range(50, -1, -1): #This will start from 50 going down to 0
    print (int)
print("Done!")

# This loop follows three arguments for the range feature: (x, y, z) 
#   x= starting value
#   y= ending value
#   z= step value

# 30 to 50 in increments of 1
print("Starting to count up from 30 to 50...")
for int in range(30, 51): #This starts at 30 going up to 50
    print (int)
print("Done!")

# 50 to 10 in decrements of 2
print("Starting to count down from 50 to 10...")
for int in range(50, 9, -2): #This starts at 50 ending at 10
    print(int)
print("Done!")

# Why 9 and not 10?
# Placing 9 as an ending value makes the program print 10 as the last number.

# 100 to 200 in increments of 5
print("Starting to count up from 100 to 200 ")
for int in range(100, 201, 5): #This starts from 100 to 200
    print(int)
print("Done!")

# Explanation: From these loops, the range function is used with the for loop
#              simplifying the proess of writing a for loop program

```


______________________________________________________________________________________


## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.

### Result:
```python
#Program

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Dave"]

name_search = "Sam"   #This tells the program the name we want to search in the list

#if-else statement checks whether the name is on the list or not
if name_search in list_of_names:
    print(f'{name_search} is in the list.')

else:
    print(f'{name_search} is not in the list.')

# Output:
# When Sam is in the list:
# - "Sam is in the list."
# When Sam is not on the list:
# - "Sam is not in the list."

#Optional Requirement

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Dave"]

ask_user = input("Enter a name you want to search for: ") #This specifically tells the program the name we want to search in the list

#if-else statement checks whether the name is on the list or not
if ask_user in list_of_names:
    print(f'{ask_user} is in the list.')

else:
    print(f'{ask_user} is not in the list.')

#Output: 
# Enter a name you want to search for: Jake
# Jake is in the list.

# Enter a name you want to search for: Achi
# Achi is not in the list.
```
_______________________________________________________________________________________


## Exercise 9: Hello - 10 Marks

Fill in the blanks in the code below so that the function hello() prints "Hello" to the console.
```python

def hello():
    ____  # Fill in this blank to print "Hello" to the console

def main():
    ____  # Fill in this blank to call the hello() function

if __name__ == "__main__":
    main()
```
### Result:
```python
#Program

def hello():
    print ("Hello!") # This will print "Hello" to the console

def main():
    hello() # This will call the function hello()

if __name__ == "__main__":
    main() # Lastly, this is the function which will run the main()

#Output:

# Hello!
```
________________________________________________________________________________________

## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.

### Result:
```python
# Program

def check_even_odd(number):
    """Checks if a number is even or odd"""
    return "Even" if number %2 == 0 else "Odd"

def main():
    ask_number = int(input("Enter a number: ")) #This asks the user for a number
    result = check_even_odd(ask_number) #This will check whether the user inputs an even or odd number
    print(result) #Program will output either Even or Odd depending on what the user inputted.

if __name__ == "__main__":  
    main()   #Applying this ensures that the program is runned directly, not when its imported

#Output: 
# Enter a number: 5
# Odd

# Enter a number: 2
# Even
```
